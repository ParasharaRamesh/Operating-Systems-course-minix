import random

w3List=[]

def createAllProblems():
    allThreeLetterWords = "aahaalaasabaaboabsabyaceactaddadoadsadzaffaftagaageagoagsahaahiahsaidailaimainairaisaitalaalbaleallalpalsaltamaamiampamuanaandaneaniantanyapeapoappaptarbarcarearfarkarmarsartashaskaspassateattaukavaaveavoawaaweawlawnaxeayeaysazobaabadbagbahbalbambanbapbarbasbatbaybedbeebegbelbenbesbetbeybibbidbigbinbiobisbitbizboabobbodbogboobopbosbotbowboxboybrabrobrrbubbudbugbumbunburbusbutbuybyebyscabcadcamcancapcarcatcawcayceecelcepchicigciscobcodcogcolconcoocopcorcoscotcowcoxcoycozcrucrycubcudcuecumcupcurcutcwmdabdaddagdahdakdaldamdandapdawdaydebdeedefdeldendevdewdexdeydibdiddiedifdigdimdindipdisditdocdoedogdoldomdondordosdotdowdrydubdudduedugduhduidunduodupdyeeareateauebbecuedhedseekeeleffefsefteggegoekeeldelfelkellelmelsemeemsemuendengenseoneraereergernerrersessetaetheveeweeyefabfadfagfanfarfasfatfaxfayfedfeefehfemfenferfesfetfeufewfeyfezfibfidfiefigfilfinfirfitfixfizfluflyfobfoefogfohfonfopforfoufoxfoyfrofryfubfudfugfunfurgabgadgaegaggalgamgangapgargasgatgaygedgeegelgemgengetgeyghigibgidgiegiggingipgitgnugoagobgodgoogorgosgotgoxgoygulgumgungutguvguygymgyphadhaehaghahhajhamhaohaphashathawhayhehhemhenhepherheshethewhexheyhichidhiehimhinhiphishithmmhobhodhoehoghonhophoshothowhoyhubhuehughuhhumhunhuphuthypiceichickicyidsiffifsiggilkillimpinkinninsionireirkismitsivyjabjagjamjarjawjayjeejetjeujewjibjigjinjobjoejogjotjowjoyjugjunjusjutkabkaekafkaskatkaykeakefkegkenkepkexkeykhikidkifkinkipkirkiskitkoakobkoikopkorkoskuekyelablacladlaglamlaplarlaslatlavlawlaxlaylealedleelegleileklesletleulevlexleylezliblidlielinliplislitlobloglooloplotlowloxluglumluvluxlyemacmadmaemagmanmapmarmasmatmawmaxmaymedmegmelmemmenmetmewmhomibmicmidmigmilmimmirmismixmoamobmocmodmogmolmommonmoomopmormosmotmowmudmugmummunmusmutmycnabnaenagnahnamnannapnawnaynebneenegnetnewnibnilnimnipnitnixnobnodnognohnomnoonornosnotnownthnubnunnusnutoafoakoaroatobaobeobiocaodaoddodeodsoesoffoftohmohoohsoilokaokeoldoleomsoneonoonsoohootopeopsoptoraorborcoreorsortoseoudouroutovaoweowlownoxooxypacpadpahpalpampanpapparpaspatpawpaxpaypeapecpedpeepegpehpenpepperpespetpewphiphtpiapicpiepigpinpippispitpiupixplypodpohpoipolpompoopoppotpowpoxproprypsipstpubpudpugpulpunpuppurpusputpyapyepyxqatqisquaradragrahrairajramranraprasratrawraxrayrebrecredreerefregreiremrepresretrevrexrhoriaribridrifrigrimrinriprobrocrodroeromrotrowrubruerugrumrunrutryaryesabsacsadsaesagsalsapsatsausawsaxsayseasecseesegseiselsensersetsewsexshasheshhshysibsicsimsinsipsirsissitsixskaskiskyslysobsodsolsomsonsopsossotsousowsoxsoyspaspysristysubsuesuksumsunsupsuqsyntabtadtaetagtajtamtantaotaptartastattautavtawtaxteatedteetegteltentettewthethothytictietiltintiptistittodtoetogtomtontootoptortottowtoytrytsktubtugtuituntuptuttuxtwatwotyeudoughukeuluummumpunsupoupsurburdurnurpuseutauteutsvacvanvarvasvatvauvavvawveevegvetvexviavidvievigvimvisvoevowvoxvugvumwabwadwaewagwanwapwarwaswatwawwaxwaywebwedweewenwetwhawhowhywigwinwiswitwizwoewogwokwonwoowopwoswotwowwrywudwyewynxisyagyahyakyamyapyaryawyayyeayehyenyepyesyetyewyidyinyipyobyodyokyomyonyouyowyukyumyupzagzapzaszaxzedzeezekzepzigzinzipzitzoazoozuzzzz"
    for i in range (0,(len(allThreeLetterWords)-2)/3):
        w3List.append(allThreeLetterWords[3*i:(3*i)+3])
    
def generateProblem():
    return w3List[random.randint(0, len(w3List)-1)]

def asCharList(s):
    answer = []
    for c in s:
        answer.append(c)
    return answer

def score(guess):    
    bulls = 0
    cows = 0
    p = asCharList(theProblem)
    g = asCharList(guess)
    for x in range(len(g)):
        if p[x] == g[x]:
            bulls += 1
        elif g[x] in p:
            cows += 1
    return (bulls, cows)

createAllProblems()
theProblem = generateProblem()
chances=25
for i in range(chances):
    currguess= str(input('Enter your guess> '))
    if currguess == 'QUIT':
        break;
    b, c = score(currguess)
    if b == 3:
        print ('Bravo ! You got it in ' + str(i+1) + ' chances!')
        break;
    else:
        print ('Bulls =' + str(b) + ' and Cows = ' + str(c))
if currguess == 'QUIT':
    print ('The word was ' + theProblem)
elif b != 3:
    print ('You exhausted your chances. The word was ' + theProblem)

    

                
            

        
    
    
    
