import codewars_test as test
from main import proofread

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals( proofread("SHe wEnt CaNoIenG."), "She went canoeing.")
        test.assert_equals( proofread("He haD iEght ShOTs of CAffIEne"), "He had eight shots of caffeine")
        test.assert_equals( proofread("THe neIghBour's ceiLing FEll on His Head. The WiEght of It crusHed him To thE gROuNd."), "The neighbour's ceiling fell on his head. The weight of it crushed him to the ground.")
        test.assert_equals( proofread("ThE kiDs enJoYEd the SLiegh RidE."), "The kids enjoyed the sleigh ride.")
        test.assert_equals( proofread("SHE did NOT diegn to GUESS her NIEGHBOUR'S wieght."), "She did not deign to guess her neighbour's weight.")
        test.assert_equals( proofread("They had to fIEgn thIEr appreciation for her bIEge tights."), "They had to feign their appreciation for her beige tights.")
        test.assert_equals( proofread("Niether of the fencers wanted to forfiet the match. They both expected to sieze victory."), "Neither of the fencers wanted to forfeit the match. They both expected to seize victory.")
        test.assert_equals( proofread("Protien intAkE miGHt afFect aNy pOteNtIaL wieght LOSs."), "Protein intake might affect any potential weight loss." )
        test.assert_equals( proofread("MargArEt cAn't eVen concIEve of foRegOing the pARty to finisH her paPEr."), "Margaret can't even conceive of foregoing the party to finish her paper." )
        test.assert_equals( proofread("IN the wINter, it's NICE to gO for a sliegh rIDe"), "In the winter, it's nice to go for a sleigh ride")
        test.assert_equals( proofread("The mAN's ONly pURpose in lIFe is to decIEve his wIFe."), "The man's only purpose in life is to deceive his wife.")
        test.assert_equals( proofread("She LifTeD heR ViEL. The ShIeK LooKeD aT hER ExPeCtAnTlY"), "She lifted her veil. The sheik looked at her expectantly")
        test.assert_equals( proofread("PetEr Was Not Sure of WHAt he WAs sEIEng. HE had To RIEn in HIs SHock."), "Peter was not sure of what he was seeing. He had to rein in his shock." )
        test.assert_equals( proofread("That is OnE lonG frieghT traiN thAt's Blocking The Railway Crossing."), "That is one long freight train that's blocking the railway crossing.")
        test.assert_equals( proofread(""), "")