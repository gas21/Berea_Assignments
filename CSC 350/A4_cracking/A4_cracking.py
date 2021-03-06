# CSC 350 Computer Security
# Assignment 4 https://docs.google.com/document/d/1TiZi-7qda_Ywc76z35KEPdVKvhqBDZLHwlaaAXF5a7c
# Author Soe Win Han

from math import log, sqrt


def crack(text, r):
    """Crack the cipher text encrypted with a square matrix."""
    return ''.join(letter for j in zip(*[text[i*r:i*r+r] for i in range(r)]) for letter in j)


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    words = open("A4-words-by-frequency.txt").read().split()
    wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
    maxword = max(len(x) for x in words)

    def best_match(i):
        # Find the best match for the i first characters, assuming cost has
        # been built for the i-1 first characters.
        # Returns a pair (match_cost, match_length).
        # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).

        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k, c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i > 0:
        c, k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


if __name__ == "__main__":
    text1 = "coovhsrerotovoaaaowednphrtyadertfeeikwualstratflknfsfrlrilsnwpjyhefwuereowonknhteutliwafitiysoriowohbdsspegbiaallhafmtieiaiaudtdouooelhnssrrurniateaddelrnkitindkoelweuieasierplnrloiekoaiemlininmhrurrudlittnymrogsbenlmidtaeinnriiekaenegsrihbeeaoeokonoerrddeeneldeaolsqyiishooiianwelniordlanrnioendetsdiwhpesulkruowuokewmykobtsatfeitmduuornwemthnggieetfvpoykdnuttdghphotteiafifebisdenwibnuoenrhonoorttebeiueehmeradowtobeherweewopeaafeienhwetrteftegeyldnfoesudtaiudtrswhoemtvcviirevtfihnirelanlsannllnofnlteomeroslhhhmrlyeylrtmchistfhttaiwnyeetetgesehrtierisylelptooyfdraoihrursofieiitreperotiaroanitoehasnnolagorehnpaaohtadnrfiroacnraastlnbaelpbtlsdsnoppaanuoscpmvssoucanigetigorwlttoctmiontterniprhowdnhhlietpdrliimoidurluhngnphrpeui1natdptrlnrtaaayenomttwdhoseenoreeeehaeftriahaesfefsttaasanoeuealtrr5dmmtshyoeetnnbrrdlyhmnieitsnelossgnogflsttualenetfaholcelnthtniaogr0merhwaeboeodtcismdliremntihovltisiougjabyhsvidoeainefieoloovtonideelyrpiitaifqgceovariasprloincheyottaureotaoaeenimrbsecpnmwrtmeiienoolisarstshtiuoadaeppwdvrnortiuertupungadrocfdonenoeomxoaeeniryrntgttnenetaicptdnidmttreriieaoowsltdnetlnbhgodnkebwuvdrslopurpnegebygsoshivelhlshehoqtoeotstaswrlnkesltiesounlooushrxenzoeetiranrrtrharwoiemioasfeibolanueardooslhiyioigtwldvtfmeufytmieaeezomhsctrtoaiqtloenpsrsnnydpnowlttianaorfhitsbnenioaeneitmdetofrsmmnrlmieiparetysusltlastpjltoeeelnsswrgomtebonohoesgankftrnhemshuopbaiswemshnrlorsdiiuyhlfworoyiuptitetioyrtehvrpemtuiuaneeitdgetrsialrarniedaeapoctsmotermetaitabdskosnorhtraehnieimeaotlhtbdhshitctptsslackitlutdsecoporeoterrhlthlyonnshtniemkneelsatrlkcilholeihadeaorutsolkantlpeocaeiarpswlapsesceiottoiohotsroytreilipleoqtenuamftasgtanhuwitbgiottwecslurrinylrpcehtnuhiwtpawwapwlosanasroamueseeduowntehlearinhltncohnaesrsyatedtaeummrekitmemtnamrnookvtchamcpelrrioprayiaeiateneeehgotiesieuesltryeltsorainsardaceseaenseihhcliololeidwsystnnfnspdgpmbaouhsrefsnoqianoristupiwojtphnarablrgitneeoismawysgnnhoyhgdleiamaioitnrobndyadwunlnunnhosrniwotressspaiwelcgfclnspinothieouoittoslrepnmrpissiotoroniekodaeomtassmbearbetucnerlhtikueolneuittruiunehotyrtriedateernouewerioiytwpealthrbnleriinkelaynhremewaarwnnantfhgsurumohonnirsibdobhnnreswgoeeirciatpediioslmwilsfoesrblnibohgoyoiyimtmmnatalftdrptaweeaotwienuuelnlhntorcannthlratwiawoteilenohamwbnnotriprnjitooinoewrosedwheveeewnlbeeeicaaneihawprshtrcwpdaortuytroeogutpnspeosinrgitrasupsnieleirsadioamloolutwpelirdnahtonlswiwotespwanasirgirdrdtgtotwcsblietsclhsnsnitlvronmisyesrltasotiomeahiwhwtswrnuothnattaomesehtshhnednxntuiaenntnstepohpneelwwrhlatdnoercitianhtraetntogleslwrftdeiqeiannipaorddenotghosrkeleialiaetisaoksoaerhsteiholriohwtishinpiosfmunnittniirtbaintomantaiaailhitsthnfpytinlitmhdrseninfneohntenerntqjhiitlevgrlyaelgogcrrhhlndibiwwclueeoaohlhowaytowpugnouocweeiaeraiauoorghemomeeeitoeteopdeeigdnekeihyrfprluilenanboyeahwenlnancyndnyltlarmeoedaorddsntotrtmrllcnarbgelsainaawiwsywenderorrtilopogeaegooeielwdeltftpmpaioaekteseaylueteryblhtntkuanaitaotsseuerhtohleergltnwanlaksooiihairnmfnrrhaablarsttsioeittgoesrdnsalneutgmcoehoeusehelhttheycowwvtrerfadtfdroelsaibethhstuitoeatmedrtgkktdsgieltniksmrlioiihhyudkwhnehsrtylgotjeuplhcnlpoieeirnscnthuasomeeshtpisaowotmnaeltwnseaomeonaelotewoiothopniyakeolmscsspgnodtespmmrtsoeoertnshrmaogsosngictuncfetrympiiunnheildcmmtsoaeiaahamomaeptureptcfsbnlemiawyttetmteasossoemrktpelftpeeetnattreowdcrsmmrrytpnneanptriufeedbrinteledmiihrnyuwtwaowihlaaihuetpwechupdmeyeebeaadoeltdtcorhansstaeyasfigayernseidonhulsveneunchitsoeideerrlyertnorniowaanashwaelgttolrmcsopidiapgtcnhutanoeeldnmdeatfnmrgtibeaoptehtlaslnnsionhenlpitoawusyomruaekdrmeaeiretnodmlooaiwdsooecehtaololapeetttwabynttoyeianomgnmusmrlrnsnharrgvtnriekaehfrgdanbutehsetcwikaslprohaatotihcpernleoeeebnippucbdoelppeetitcdnnnetweisterptekbhknnscsaasnanytsogiahsneiisrlreddlrnhlewsiroorinhahodtsaemstnamiidileoeeaeucrtitdsesposnemolnmibetreeaacauaahnalwmnerliwwwhlgrchakinsbcenfrwtmgerhssipnmatitdrnodnlyfojrfilhseddeellnrgoolmlhaekipoaialimekehtpehramoeiinedrdosboponroltttairnimewtestiyeptcwajoessiarvtlnlnapedehalipretstngraptnblerngotyhfhctotnrdhharhnprrhlsduondasnaeiediekuditeulsrpnfaotbsnrhtoasaopmpseoekfmtepnaadeeeataeoieskiuhtblrtdvosestnassifartomweeotaehlmmltaerealahlmhprottpsparhlcctatmpephliehtonprhhckhetelairenrhnilseteriauoerrlueooeaatssatllreiakudaautraundahovaeieheoiseiysypeciamiebobpnpsfpgmodtanoulhuwriulorngappstrooteetdamossnbospghtndioerintanponrreuebaecwiattwsiahhrnmrteeeliaheciblplhbtflsaguiaaoameotutwtdtqeylmiaynaoraoeekiynenlwaoraiihyranreihtaoroeebetesucrqntrrleomsiyaeuettrtlowplenmdnenpeiefhtteggveeertrwvabboeooeiesdtpkiudadposwrhtrdnaxhopiiuhatdtebcsgyrmnaaswmehemspmhoaeselkfknnrwtoiteniuslroinpohaedlconrsntalotmoyeodt"
    text2 = 'aohpdnxnrilitxdsnefxxnogtfxxomceexxweolrxxftmyexx'
    c, d = int(sqrt(len(text1))), int(sqrt(len(text2)))
    a, b = crack(text1, c), crack(text2, d)
    print(infer_spaces(a))
    print(infer_spaces(b))
