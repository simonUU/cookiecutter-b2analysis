# -*- coding: utf-8 -*-
""" Sample reconstruction

Reconstruction of {{cookiecutter.project_name}}

    {{cookiecutter.project_short_description}}

This is the reconstruction code for B->K*gamma as an example.
It should demonstrate some of the features of modular analysis.


Authors:
    {{cookiecutter.full_name}} ({{cookiecutter.email}})
    //Simon (simon.wehle@desy.de)


"""

from ROOT import Belle2
import basf2 as b2
import modularAnalysis as ma
from variables import variables
import variables.collections as vc
import variables.utils as vu


def setup():
    # b2.use_central_database("GT")
    pass


def get_variables():
    variables.addAlias("Rank_deltaE", "extraInfo(Rank_deltaE)")

    gamma_vars = vc.mc_truth + vc.kinematics + vc.cluster
    k_pi_vars = vc.pid + vc.mc_truth + vc.kinematics + vc.inv_mass

    kst_vars = vc.mc_truth + vc.kinematics + vc.inv_mass + ["decay_hash"] \
               + vu.create_daughter_aliases(k_pi_vars, 0, prefix='K', include_indices=False) \
               + vu.create_daughter_aliases(k_pi_vars, 1, prefix='pi', include_indices=False)

    cs_vars = vc.event_shape

    all_vars = vc.deltae_mbc + vc.mc_truth + vc.kinematics \
               + vu.create_daughter_aliases(kst_vars, 0, prefix='Kst', include_indices=False) \
               + vu.create_daughter_aliases(gamma_vars, 1, prefix='gamma', include_indices=False) \
               + ["decay_hash", "chiProb", "Rank_deltaE", "isExtendedSignal", "SignalRegion"] \
               + vc.recoil_kinematics \
               + cs_vars
    return all_vars


def reconstruct(infile='default.root', outfile='output_beta.root', path=None):
    """

    Args:
        infile: Input file name (use overwrite from basf2)
        outfile: output file name (use overwrite from basf2)
        path: (optional) basf2 path

    Returns:
        path
    """

    setup()

   # EXAMPE RECONSTRUCTION CODE
   # DELETE OR MODIFY FROM HERE
    just_an_example = True
    if just_an_example:
        with open(outfile, 'w') as f:
            f.write("Proccessed example input " + infile)
    else:
        path = b2.create_path() if path is None else path

        # Input file
        ma.inputMdstList("default", infile, path=path)

        # Event level cuts examples
        ma.applyEventCuts('R2EventLevel<0.6 and nTracks>=3', path=path)

        #
        # Load Primary particles
        #
        from stdPhotons import stdPhotons
        stdPhotons('cdc', path)
        ma.cutAndCopyList('gamma:sig', 'gamma:cdc', 'clusterNHits > 1.5 and E > 1.5', True, path)

        from stdPi0s import stdPi0s
        stdPi0s('eff20', path)

        # Loading charged tracks
        good_track = 'thetaInCDCAcceptance and nCDCHits>20 and dr < 0.5 and abs(dz) < 2'
        ma.fillParticleList("pi+:sig", good_track + " and pionID > 0.0", path=path)
        ma.fillParticleList("K+:sig", good_track + " and kaonID > 0.0", path=path)

        #
        # Combine particles
        #
        ma.reconstructDecay('K*0:sig  -> K+:sig pi-:sig', '0.6 < M < 1.6', path=path)

        ma.reconstructDecay('B0:sig ->  K*0:sig gamma:sig', '5.22 < Mbc < 5.3 and  abs(deltaE)< 1', path=path)

        # Final Calculateions
        ma.rankByHighest("B0:ch1", "formula(-1*abs(deltaE))", outputVariable='Rank_deltaE', path=path)

        ma.buildEventShape(allMoments=True, path=path)

        ma.matchMCTruth("B0:sig", path=path)

        # 
        # Write out Ntuples
        #
        all_vars = get_variables()
        ma.variablesToNtuple('B0:ch1', all_vars, filename=outfile, treename="B0", path=path)
    # TO HERE

    #ma.printMCParticles(path=path)
    return path


if __name__ == "__main__":
    # If file is run standalone

    env = Belle2.Environment.Instance()
    override = env.getOutputFileOverride()
    filename = "output.root" if override == "" else override
    path = reconstruct("default.root", filename)
    b2.process(path)
    print(b2.statistics)
