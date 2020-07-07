from matplotlib.colors import ListedColormap

__author__ = "Ellert van der Velden (@1313e)"

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [1.93509327e-04, 2.50024184e-04, 2.34566888e-04],
           [6.45783269e-04, 8.78079237e-04, 8.12470819e-04],
           [1.29010993e-03, 1.84048334e-03, 1.67902967e-03],
           [2.09146283e-03, 3.12127607e-03, 2.80698432e-03],
           [3.02526281e-03, 4.71219923e-03, 4.17682685e-03],
           [4.07249701e-03, 6.60860152e-03, 5.77279387e-03],
           [5.21756433e-03, 8.80790932e-03, 7.58132768e-03],
           [6.44725394e-03, 1.13088483e-02, 9.59033689e-03],
           [7.75007645e-03, 1.41110388e-02, 1.17887802e-02],
           [9.11601638e-03, 1.72146761e-02, 1.41664457e-02],
           [1.05359012e-02, 2.06205143e-02, 1.67137198e-02],
           [1.20015462e-02, 2.43296140e-02, 1.94215344e-02],
           [1.35054808e-02, 2.83433169e-02, 2.22812634e-02],
           [1.50408443e-02, 3.26631877e-02, 2.52846614e-02],
           [1.66012774e-02, 3.72909807e-02, 2.84238087e-02],
           [1.81808045e-02, 4.21768152e-02, 3.16910529e-02],
           [1.97739218e-02, 4.70388494e-02, 3.50790238e-02],
           [2.13754403e-02, 5.18604855e-02, 3.85805712e-02],
           [2.29804337e-02, 5.66454030e-02, 4.21385506e-02],
           [2.45842593e-02, 6.13968237e-02, 4.56086941e-02],
           [2.61825162e-02, 6.61175930e-02, 4.90002110e-02],
           [2.77710234e-02, 7.08102397e-02, 5.23159965e-02],
           [2.93460796e-02, 7.54769443e-02, 5.55587456e-02],
           [3.09037223e-02, 8.01197917e-02, 5.87307206e-02],
           [3.24402777e-02, 8.47406284e-02, 6.18339983e-02],
           [3.39526161e-02, 8.93410306e-02, 6.48705944e-02],
           [3.54372888e-02, 9.39225491e-02, 6.78421714e-02],
           [3.68911025e-02, 9.84865700e-02, 7.07502748e-02],
           [3.83114187e-02, 1.03034268e-01, 7.35964596e-02],
           [3.96949203e-02, 1.07566901e-01, 7.63818609e-02],
           [4.10270748e-02, 1.12085405e-01, 7.91078690e-02],
           [4.22852722e-02, 1.16590876e-01, 8.17753688e-02],
           [4.34796369e-02, 1.21084105e-01, 8.43855501e-02],
           [4.46105683e-02, 1.25566035e-01, 8.69391266e-02],
           [4.56794258e-02, 1.30037336e-01, 8.94371255e-02],
           [4.66864932e-02, 1.34498821e-01, 9.18801279e-02],
           [4.76327496e-02, 1.38951101e-01, 9.42689409e-02],
           [4.85186436e-02, 1.43394834e-01, 9.66041341e-02],
           [4.93446637e-02, 1.47830612e-01, 9.88862590e-02],
           [5.01115107e-02, 1.52258940e-01, 1.01115921e-01],
           [5.08193088e-02, 1.56680386e-01, 1.03293470e-01],
           [5.14686058e-02, 1.61095396e-01, 1.05419396e-01],
           [5.20596814e-02, 1.65504426e-01, 1.07494060e-01],
           [5.25926754e-02, 1.69907923e-01, 1.09517739e-01],
           [5.30679860e-02, 1.74306254e-01, 1.11490793e-01],
           [5.34856950e-02, 1.78699810e-01, 1.13413432e-01],
           [5.38458863e-02, 1.83088953e-01, 1.15285847e-01],
           [5.41487883e-02, 1.87473993e-01, 1.17108263e-01],
           [5.43944101e-02, 1.91855254e-01, 1.18880799e-01],
           [5.45827497e-02, 1.96233034e-01, 1.20603547e-01],
           [5.47138805e-02, 2.00607601e-01, 1.22276610e-01],
           [5.47877800e-02, 2.04979216e-01, 1.23900033e-01],
           [5.48043701e-02, 2.09348129e-01, 1.25473817e-01],
           [5.47636127e-02, 2.13714566e-01, 1.26997958e-01],
           [5.46654306e-02, 2.18078741e-01, 1.28472417e-01],
           [5.45097140e-02, 2.22440860e-01, 1.29897119e-01],
           [5.42963722e-02, 2.26801108e-01, 1.31271973e-01],
           [5.40252253e-02, 2.31159671e-01, 1.32596830e-01],
           [5.36961898e-02, 2.35516707e-01, 1.33871555e-01],
           [5.33091605e-02, 2.39872366e-01, 1.35095978e-01],
           [5.28639041e-02, 2.44226805e-01, 1.36269847e-01],
           [5.23603371e-02, 2.48580150e-01, 1.37392945e-01],
           [5.17984200e-02, 2.52932513e-01, 1.38465036e-01],
           [5.11779138e-02, 2.57284022e-01, 1.39485769e-01],
           [5.04987586e-02, 2.61634778e-01, 1.40454829e-01],
           [4.97610672e-02, 2.65984854e-01, 1.41371923e-01],
           [4.89646087e-02, 2.70334359e-01, 1.42236578e-01],
           [4.81095025e-02, 2.74683359e-01, 1.43048405e-01],
           [4.71960904e-02, 2.79031895e-01, 1.43807045e-01],
           [4.62241055e-02, 2.83380069e-01, 1.44511834e-01],
           [4.51942343e-02, 2.87727889e-01, 1.45162407e-01],
           [4.41069195e-02, 2.92075391e-01, 1.45758218e-01],
           [4.29622767e-02, 2.96422646e-01, 1.46298503e-01],
           [4.17617776e-02, 3.00769608e-01, 1.46782907e-01],
           [4.05056178e-02, 3.05116356e-01, 1.47210466e-01],
           [3.91860415e-02, 3.09462832e-01, 1.47580723e-01],
           [3.78394662e-02, 3.13809060e-01, 1.47892774e-01],
           [3.64719515e-02, 3.18155009e-01, 1.48145882e-01],
           [3.50887198e-02, 3.22500648e-01, 1.48339195e-01],
           [3.36952984e-02, 3.26845945e-01, 1.48471787e-01],
           [3.22977241e-02, 3.31190846e-01, 1.48542721e-01],
           [3.09025193e-02, 3.35535281e-01, 1.48551031e-01],
           [2.95161009e-02, 3.39879208e-01, 1.48495479e-01],
           [2.81467098e-02, 3.44222474e-01, 1.48375306e-01],
           [2.68005354e-02, 3.48565098e-01, 1.48188650e-01],
           [2.54873927e-02, 3.52906861e-01, 1.47934848e-01],
           [2.42156992e-02, 3.57247672e-01, 1.47612357e-01],
           [2.29941383e-02, 3.61587447e-01, 1.47219394e-01],
           [2.18337857e-02, 3.65925962e-01, 1.46754848e-01],
           [2.07452934e-02, 3.70263056e-01, 1.46217042e-01],
           [1.97393466e-02, 3.74598595e-01, 1.45603863e-01],
           [1.88284625e-02, 3.78932355e-01, 1.44913560e-01],
           [1.80260069e-02, 3.83264091e-01, 1.44144275e-01],
           [1.73458437e-02, 3.87593564e-01, 1.43293824e-01],
           [1.68028057e-02, 3.91920511e-01, 1.42359870e-01],
           [1.64127786e-02, 3.96244643e-01, 1.41339910e-01],
           [1.61927954e-02, 4.00565644e-01, 1.40231262e-01],
           [1.61611400e-02, 4.04883167e-01, 1.39031053e-01],
           [1.63374640e-02, 4.09196828e-01, 1.37736202e-01],
           [1.67429164e-02, 4.13506210e-01, 1.36343403e-01],
           [1.74002872e-02, 4.17810852e-01, 1.34849113e-01],
           [1.83337724e-02, 4.22110272e-01, 1.33249244e-01],
           [1.95690775e-02, 4.26403971e-01, 1.31539013e-01],
           [2.11359806e-02, 4.30691270e-01, 1.29714654e-01],
           [2.30645534e-02, 4.34971568e-01, 1.27770436e-01],
           [2.53884611e-02, 4.39244134e-01, 1.25700817e-01],
           [2.81441623e-02, 4.43508177e-01, 1.23499538e-01],
           [3.13720704e-02, 4.47762776e-01, 1.21160355e-01],
           [3.51144835e-02, 4.52007048e-01, 1.18674245e-01],
           [3.94202122e-02, 4.56239839e-01, 1.16033700e-01],
           [4.41743104e-02, 4.60459942e-01, 1.13229183e-01],
           [4.92091629e-02, 4.64665999e-01, 1.10249993e-01],
           [5.45263389e-02, 4.68856472e-01, 1.07084286e-01],
           [6.01204801e-02, 4.73029658e-01, 1.03717652e-01],
           [6.59897621e-02, 4.77183563e-01, 1.00135070e-01],
           [7.21352511e-02, 4.81315924e-01, 9.63190793e-02],
           [7.85610931e-02, 4.85424148e-01, 9.22494352e-02],
           [8.52747785e-02, 4.89505253e-01, 8.79016445e-02],
           [9.22873950e-02, 4.93555741e-01, 8.32479349e-02],
           [9.96135671e-02, 4.97571498e-01, 7.82569642e-02],
           [1.07271802e-01, 5.01547686e-01, 7.28918112e-02],
           [1.15285355e-01, 5.05478564e-01, 6.71075132e-02],
           [1.23682318e-01, 5.09357259e-01, 6.08518275e-02],
           [1.32494669e-01, 5.13175577e-01, 5.40676995e-02],
           [1.41760365e-01, 5.16923679e-01, 4.66866189e-02],
           [1.51519352e-01, 5.20589962e-01, 3.86341799e-02],
           [1.61809569e-01, 5.24161140e-01, 3.05165911e-02],
           [1.72659668e-01, 5.27622767e-01, 2.29573971e-02],
           [1.84070263e-01, 5.30961229e-01, 1.62666445e-02],
           [1.95990150e-01, 5.34167430e-01, 1.08421311e-02],
           [2.08292268e-01, 5.37242141e-01, 7.13645494e-03],
           [2.20768579e-01, 5.40200728e-01, 5.57218325e-03],
           [2.33172666e-01, 5.43071852e-01, 6.42421816e-03],
           [2.45285674e-01, 5.45889887e-01, 9.75877890e-03],
           [2.56965338e-01, 5.48685624e-01, 1.54659294e-02],
           [2.68149795e-01, 5.51481511e-01, 2.33460961e-02],
           [2.78834836e-01, 5.54291600e-01, 3.31845843e-02],
           [2.89048638e-01, 5.57123539e-01, 4.45920583e-02],
           [2.98832470e-01, 5.59980976e-01, 5.59255823e-02],
           [3.08230659e-01, 5.62865168e-01, 6.68856579e-02],
           [3.17285543e-01, 5.65776056e-01, 7.74958657e-02],
           [3.26035791e-01, 5.68712822e-01, 8.77902035e-02],
           [3.34514511e-01, 5.71674559e-01, 9.78029595e-02],
           [3.42751903e-01, 5.74659928e-01, 1.07567999e-01],
           [3.50773320e-01, 5.77667789e-01, 1.17114915e-01],
           [3.58601296e-01, 5.80696909e-01, 1.26470552e-01],
           [3.66253769e-01, 5.83746550e-01, 1.35656299e-01],
           [3.73748785e-01, 5.86815420e-01, 1.44693924e-01],
           [3.81100640e-01, 5.89902716e-01, 1.53600506e-01],
           [3.88322051e-01, 5.93007678e-01, 1.62391127e-01],
           [3.95424488e-01, 5.96129548e-01, 1.71079332e-01],
           [4.02418180e-01, 5.99267621e-01, 1.79677126e-01],
           [4.09310901e-01, 6.02421648e-01, 1.88193052e-01],
           [4.16112177e-01, 6.05590658e-01, 1.96638555e-01],
           [4.22827745e-01, 6.08774600e-01, 2.05019473e-01],
           [4.29464716e-01, 6.11972856e-01, 2.13343992e-01],
           [4.36028842e-01, 6.15185067e-01, 2.21618379e-01],
           [4.42525204e-01, 6.18410956e-01, 2.29848000e-01],
           [4.48958486e-01, 6.21650258e-01, 2.38037750e-01],
           [4.55333012e-01, 6.24902723e-01, 2.46192108e-01],
           [4.61652774e-01, 6.28168115e-01, 2.54315171e-01],
           [4.67921459e-01, 6.31446217e-01, 2.62410691e-01],
           [4.74142269e-01, 6.34736901e-01, 2.70481712e-01],
           [4.80317856e-01, 6.38040167e-01, 2.78530395e-01],
           [4.86451765e-01, 6.41355634e-01, 2.86560781e-01],
           [4.92546032e-01, 6.44683405e-01, 2.94574173e-01],
           [4.98603341e-01, 6.48023296e-01, 3.02573271e-01],
           [5.04625752e-01, 6.51375307e-01, 3.10559686e-01],
           [5.10615641e-01, 6.54739274e-01, 3.18535813e-01],
           [5.16574351e-01, 6.58115392e-01, 3.26502015e-01],
           [5.22504328e-01, 6.61503388e-01, 3.34461110e-01],
           [5.28407075e-01, 6.64903324e-01, 3.42414046e-01],
           [5.34283755e-01, 6.68315375e-01, 3.50361090e-01],
           [5.40136311e-01, 6.71739364e-01, 3.58304362e-01],
           [5.45966088e-01, 6.75175336e-01, 3.66244752e-01],
           [5.51774359e-01, 6.78623336e-01, 3.74183086e-01],
           [5.57562336e-01, 6.82083416e-01, 3.82120129e-01],
           [5.63331172e-01, 6.85555632e-01, 3.90056593e-01],
           [5.69081963e-01, 6.89040044e-01, 3.97993136e-01],
           [5.74815748e-01, 6.92536719e-01, 4.05930355e-01],
           [5.80533536e-01, 6.96045720e-01, 4.13868855e-01],
           [5.86236263e-01, 6.99567126e-01, 4.21809115e-01],
           [5.91924836e-01, 7.03101016e-01, 4.29751631e-01],
           [5.97600121e-01, 7.06647471e-01, 4.37696844e-01],
           [6.03262943e-01, 7.10206578e-01, 4.45645158e-01],
           [6.08914091e-01, 7.13778430e-01, 4.53596944e-01],
           [6.14554321e-01, 7.17363122e-01, 4.61552539e-01],
           [6.20184357e-01, 7.20960755e-01, 4.69512249e-01],
           [6.25804826e-01, 7.24571468e-01, 4.77476160e-01],
           [6.31416229e-01, 7.28195457e-01, 4.85444032e-01],
           [6.37019428e-01, 7.31832721e-01, 4.93416716e-01],
           [6.42615041e-01, 7.35483376e-01, 5.01394409e-01],
           [6.48203562e-01, 7.39147595e-01, 5.09376988e-01],
           [6.53785409e-01, 7.42825588e-01, 5.17364117e-01],
           [6.59361388e-01, 7.46517346e-01, 5.25356679e-01],
           [6.64931979e-01, 7.50223028e-01, 5.33354619e-01],
           [6.70497428e-01, 7.53942923e-01, 5.41357146e-01],
           [6.76058564e-01, 7.57676986e-01, 5.49365353e-01],
           [6.81615713e-01, 7.61425447e-01, 5.57378761e-01],
           [6.87169281e-01, 7.65188492e-01, 5.65397163e-01],
           [6.92719962e-01, 7.68966130e-01, 5.73421325e-01],
           [6.98267829e-01, 7.72758734e-01, 5.81449975e-01],
           [7.03813682e-01, 7.76566242e-01, 5.89484278e-01],
           [7.09357706e-01, 7.80388955e-01, 5.97523349e-01],
           [7.14900461e-01, 7.84226945e-01, 6.05567592e-01],
           [7.20442284e-01, 7.88080419e-01, 6.13616649e-01],
           [7.25983613e-01, 7.91949519e-01, 6.21670514e-01],
           [7.31524841e-01, 7.95834415e-01, 6.29729028e-01],
           [7.37066372e-01, 7.99735265e-01, 6.37792075e-01],
           [7.42608580e-01, 8.03652248e-01, 6.45859419e-01],
           [7.48151912e-01, 8.07585497e-01, 6.53931079e-01],
           [7.53696666e-01, 8.11535241e-01, 6.62006512e-01],
           [7.59243385e-01, 8.15501546e-01, 6.70086076e-01],
           [7.64792251e-01, 8.19484725e-01, 6.78168735e-01],
           [7.70343895e-01, 8.23484785e-01, 6.86255139e-01],
           [7.75898510e-01, 8.27502039e-01, 6.94344212e-01],
           [7.81456646e-01, 8.31536553e-01, 7.02436223e-01],
           [7.87018681e-01, 8.35588520e-01, 7.10530720e-01],
           [7.92584965e-01, 8.39658158e-01, 7.18627064e-01],
           [7.98156063e-01, 8.43745536e-01, 7.26725422e-01],
           [8.03732277e-01, 8.47850921e-01, 7.34824801e-01],
           [8.09314151e-01, 8.51974412e-01, 7.42925109e-01],
           [8.14902200e-01, 8.56116141e-01, 7.51026023e-01],
           [8.20496762e-01, 8.60276381e-01, 7.59126346e-01],
           [8.26098507e-01, 8.64455173e-01, 7.67226129e-01],
           [8.31707959e-01, 8.68652679e-01, 7.75324650e-01],
           [8.37325589e-01, 8.72869129e-01, 7.83420732e-01],
           [8.42952120e-01, 8.77104573e-01, 7.91514086e-01],
           [8.48588192e-01, 8.81359152e-01, 7.99603791e-01],
           [8.54234397e-01, 8.85633076e-01, 8.07688414e-01],
           [8.59891583e-01, 8.89926385e-01, 8.15767307e-01],
           [8.65560547e-01, 8.94239196e-01, 8.23839202e-01],
           [8.71242083e-01, 8.98571675e-01, 8.31902371e-01],
           [8.76937183e-01, 9.02923881e-01, 8.39955442e-01],
           [8.82646876e-01, 9.07295896e-01, 8.47996641e-01],
           [8.88372233e-01, 9.11687835e-01, 8.56023720e-01],
           [8.94114428e-01, 9.16099804e-01, 8.64034173e-01],
           [8.99874778e-01, 9.20531867e-01, 8.72025348e-01],
           [9.05654637e-01, 9.24984145e-01, 8.79993920e-01],
           [9.11455372e-01, 9.29456829e-01, 8.87935828e-01],
           [9.17278448e-01, 9.33950111e-01, 8.95846678e-01],
           [9.23125247e-01, 9.38464307e-01, 9.03721185e-01],
           [9.28996949e-01, 9.42999915e-01, 9.11553110e-01],
           [9.34894309e-01, 9.47557714e-01, 9.19335099e-01],
           [9.40817457e-01, 9.52138807e-01, 9.27059103e-01],
           [9.46765312e-01, 9.56744884e-01, 9.34716014e-01],
           [9.52734993e-01, 9.61378403e-01, 9.42296234e-01],
           [9.58721021e-01, 9.66042820e-01, 9.49790474e-01],
           [9.64714593e-01, 9.70742707e-01, 9.57191443e-01],
           [9.70702993e-01, 9.75483786e-01, 9.64495784e-01],
           [9.76669930e-01, 9.80272517e-01, 9.71706853e-01],
           [9.82597206e-01, 9.85115193e-01, 9.78837064e-01],
           [9.88467899e-01, 9.90016592e-01, 9.85908738e-01],
           [9.94270146e-01, 9.94978692e-01, 9.92951959e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

cmap = ListedColormap(cm_data, name="jungle")
