from matplotlib.colors import ListedColormap

__author__ = "Ellert van der Velden (@1313e)"

cm_type = "linear"

cm_data = [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [1.62867116e-04, 2.46906118e-04, 3.84764277e-04],
           [5.19993908e-04, 8.63609112e-04, 1.44924295e-03],
           [9.91978257e-04, 1.80186459e-03, 3.23939130e-03],
           [1.53234818e-03, 3.04049097e-03, 5.83126671e-03],
           [2.10618239e-03, 4.56526582e-03, 9.31288320e-03],
           [2.68501352e-03, 6.36471940e-03, 1.37822567e-02],
           [3.24478964e-03, 8.42841367e-03, 1.93474325e-02],
           [3.76493586e-03, 1.07460096e-02, 2.61270805e-02],
           [4.22793538e-03, 1.33066532e-02, 3.42513135e-02],
           [4.61816299e-03, 1.60984983e-02, 4.37304615e-02],
           [4.92406847e-03, 1.91082323e-02, 5.35948260e-02],
           [5.13754817e-03, 2.23207832e-02, 6.36698810e-02],
           [5.25200581e-03, 2.57187495e-02, 7.39796288e-02],
           [5.26599893e-03, 2.92820795e-02, 8.45420823e-02],
           [5.18252557e-03, 3.29875945e-02, 9.53747815e-02],
           [5.00962767e-03, 3.68084448e-02, 1.06495347e-01],
           [4.75964126e-03, 4.07080221e-02, 1.17927213e-01],
           [4.45538187e-03, 4.44750705e-02, 1.29682333e-01],
           [4.12594668e-03, 4.80574592e-02, 1.41779969e-01],
           [3.81077952e-03, 5.14374017e-02, 1.54238229e-01],
           [3.56168625e-03, 5.45935047e-02, 1.67073324e-01],
           [3.44509937e-03, 5.75004350e-02, 1.80298553e-01],
           [3.54340473e-03, 6.01271585e-02, 1.93929745e-01],
           [3.95980127e-03, 6.24374524e-02, 2.07976463e-01],
           [4.82098309e-03, 6.43888005e-02, 2.22442775e-01],
           [6.28057305e-03, 6.59318223e-02, 2.37324328e-01],
           [8.52237986e-03, 6.70081804e-02, 2.52609804e-01],
           [1.17632265e-02, 6.75524495e-02, 2.68268772e-01],
           [1.62536969e-02, 6.74900098e-02, 2.84253726e-01],
           [2.22732585e-02, 6.67426449e-02, 3.00483253e-01],
           [3.01236762e-02, 6.52266824e-02, 3.16848080e-01],
           [4.01057430e-02, 6.28670169e-02, 3.33189427e-01],
           [5.13929820e-02, 5.96086525e-02, 3.49299507e-01],
           [6.31263967e-02, 5.54241731e-02, 3.64937781e-01],
           [7.51477676e-02, 5.03344010e-02, 3.79839063e-01],
           [8.72844624e-02, 4.44105699e-02, 3.93751145e-01],
           [9.93702701e-02, 3.77796935e-02, 4.06467596e-01],
           [1.11265297e-01, 3.11190155e-02, 4.17856049e-01],
           [1.22868668e-01, 2.48888878e-02, 4.27867571e-01],
           [1.34121220e-01, 1.92876752e-02, 4.36527697e-01],
           [1.45000137e-01, 1.44324348e-02, 4.43916563e-01],
           [1.55507524e-01, 1.03728263e-02, 4.50145951e-01],
           [1.65665958e-01, 7.10022775e-03, 4.55343005e-01],
           [1.75503848e-01, 4.57595756e-03, 4.59634300e-01],
           [1.85055923e-01, 2.73638862e-03, 4.63139978e-01],
           [1.94355399e-01, 1.51036146e-03, 4.65968621e-01],
           [2.03434097e-01, 8.23163825e-04, 4.68216269e-01],
           [2.12321383e-01, 6.01260984e-04, 4.69966234e-01],
           [2.21043701e-01, 7.75122754e-04, 4.71289789e-01],
           [2.29624480e-01, 1.28071822e-03, 4.72247294e-01],
           [2.38084231e-01, 2.06016545e-03, 4.72889489e-01],
           [2.46439324e-01, 3.06382431e-03, 4.73259644e-01],
           [2.54706823e-01, 4.24370268e-03, 4.73392189e-01],
           [2.62898675e-01, 5.56154361e-03, 4.73317182e-01],
           [2.71027611e-01, 6.98049584e-03, 4.73057707e-01],
           [2.79102788e-01, 8.47102625e-03, 4.72633794e-01],
           [2.87133317e-01, 1.00058064e-02, 4.72060636e-01],
           [2.95126873e-01, 1.15614619e-02, 4.71350303e-01],
           [3.03089873e-01, 1.31181559e-02, 4.70512278e-01],
           [3.11027639e-01, 1.46592117e-02, 4.69553886e-01],
           [3.18945399e-01, 1.61694876e-02, 4.68479688e-01],
           [3.26847277e-01, 1.76367296e-02, 4.67292900e-01],
           [3.34736783e-01, 1.90507461e-02, 4.65995244e-01],
           [3.42616868e-01, 2.04032340e-02, 4.64587172e-01],
           [3.50489971e-01, 2.16876336e-02, 4.63068069e-01],
           [3.58358059e-01, 2.28990085e-02, 4.61436423e-01],
           [3.66222657e-01, 2.40339481e-02, 4.59689980e-01],
           [3.74084878e-01, 2.50904910e-02, 4.57825874e-01],
           [3.81945443e-01, 2.60680734e-02, 4.55840759e-01],
           [3.89804721e-01, 2.69674453e-02, 4.53730875e-01],
           [3.97662717e-01, 2.77906915e-02, 4.51492189e-01],
           [4.05519096e-01, 2.85412032e-02, 4.49120468e-01],
           [4.13373200e-01, 2.92236666e-02, 4.46611352e-01],
           [4.21224051e-01, 2.98440706e-02, 4.43960426e-01],
           [4.29070365e-01, 3.04097256e-02, 4.41163283e-01],
           [4.36910557e-01, 3.09292923e-02, 4.38215586e-01],
           [4.44742743e-01, 3.14128207e-02, 4.35113126e-01],
           [4.52564744e-01, 3.18718000e-02, 4.31851874e-01],
           [4.60374089e-01, 3.23192174e-02, 4.28428030e-01],
           [4.68168015e-01, 3.27696268e-02, 4.24838076e-01],
           [4.75943512e-01, 3.32391286e-02, 4.21078712e-01],
           [4.83697327e-01, 3.37454470e-02, 4.17146881e-01],
           [4.91425707e-01, 3.43085614e-02, 4.13040396e-01],
           [4.99124707e-01, 3.49501660e-02, 4.08757301e-01],
           [5.06790078e-01, 3.56940001e-02, 4.04296150e-01],
           [5.14417491e-01, 3.65654816e-02, 3.99655442e-01],
           [5.22002001e-01, 3.75929720e-02, 3.94835037e-01],
           [5.29538329e-01, 3.88072937e-02, 3.89835546e-01],
           [5.37021243e-01, 4.02410210e-02, 3.84657209e-01],
           [5.44444894e-01, 4.18899226e-02, 3.79301856e-01],
           [5.51803077e-01, 4.37735281e-02, 3.73772288e-01],
           [5.59089726e-01, 4.59131817e-02, 3.68070612e-01],
           [5.66297793e-01, 4.83260011e-02, 3.62202173e-01],
           [5.73420692e-01, 5.10249749e-02, 3.56170533e-01],
           [5.80450913e-01, 5.40213239e-02, 3.49982698e-01],
           [5.87381143e-01, 5.73224611e-02, 3.43644988e-01],
           [5.94203767e-01, 6.09329561e-02, 3.37165079e-01],
           [6.00910852e-01, 6.48546392e-02, 3.30552498e-01],
           [6.07494575e-01, 6.90863205e-02, 3.23816831e-01],
           [6.13947071e-01, 7.36243565e-02, 3.16968583e-01],
           [6.20260347e-01, 7.84629764e-02, 3.10020289e-01],
           [6.26426667e-01, 8.35943046e-02, 3.02984707e-01],
           [6.32438517e-01, 8.90087483e-02, 2.95875440e-01],
           [6.38288709e-01, 9.46952345e-02, 2.88706809e-01],
           [6.43970491e-01, 1.00641429e-01, 2.81493689e-01],
           [6.49477655e-01, 1.06833955e-01, 2.74251252e-01],
           [6.54804632e-01, 1.13258549e-01, 2.66994984e-01],
           [6.59946600e-01, 1.19900288e-01, 2.59740173e-01],
           [6.64899549e-01, 1.26743767e-01, 2.52501729e-01],
           [6.69660343e-01, 1.33773286e-01, 2.45293961e-01],
           [6.74226747e-01, 1.40973033e-01, 2.38130323e-01],
           [6.78597438e-01, 1.48327267e-01, 2.31023194e-01],
           [6.82771989e-01, 1.55820498e-01, 2.23983682e-01],
           [6.86750819e-01, 1.63437654e-01, 2.17021457e-01],
           [6.90535134e-01, 1.71164236e-01, 2.10144643e-01],
           [6.94126836e-01, 1.78986457e-01, 2.03359744e-01],
           [6.97528430e-01, 1.86891352e-01, 1.96671622e-01],
           [7.00743028e-01, 1.94866575e-01, 1.90084162e-01],
           [7.03773982e-01, 2.02901161e-01, 1.83598729e-01],
           [7.06624942e-01, 2.10985054e-01, 1.77215463e-01],
           [7.09299810e-01, 2.19109032e-01, 1.70933532e-01],
           [7.11802772e-01, 2.27264504e-01, 1.64751604e-01],
           [7.14137486e-01, 2.35444868e-01, 1.58665205e-01],
           [7.16308246e-01, 2.43643115e-01, 1.52671597e-01],
           [7.18318516e-01, 2.51854344e-01, 1.46764809e-01],
           [7.20172319e-01, 2.60073210e-01, 1.40940649e-01],
           [7.21872606e-01, 2.68296464e-01, 1.35191821e-01],
           [7.23423147e-01, 2.76519890e-01, 1.29513737e-01],
           [7.24826487e-01, 2.84741300e-01, 1.23898851e-01],
           [7.26085228e-01, 2.92958510e-01, 1.18340448e-01],
           [7.27201857e-01, 3.01169574e-01, 1.12832176e-01],
           [7.28178778e-01, 3.09372733e-01, 1.07368129e-01],
           [7.29017465e-01, 3.17567379e-01, 1.01941021e-01],
           [7.29719489e-01, 3.25752724e-01, 9.65446617e-02],
           [7.30286153e-01, 3.33928244e-01, 9.11731401e-02],
           [7.30718493e-01, 3.42093636e-01, 8.58209181e-02],
           [7.31017300e-01, 3.50248779e-01, 8.04829453e-02],
           [7.31183129e-01, 3.58393699e-01, 7.51547954e-02],
           [7.31216315e-01, 3.66528539e-01, 6.98328359e-02],
           [7.31116993e-01, 3.74653527e-01, 6.45144468e-02],
           [7.30885401e-01, 3.82768690e-01, 5.91988872e-02],
           [7.30521280e-01, 3.90874418e-01, 5.38864433e-02],
           [7.30024077e-01, 3.98971235e-01, 4.85793411e-02],
           [7.29393274e-01, 4.07059514e-01, 4.32830834e-02],
           [7.28628447e-01, 4.15139444e-01, 3.80102295e-02],
           [7.27729200e-01, 4.23211108e-01, 3.30725763e-02],
           [7.26694134e-01, 4.31275288e-01, 2.85785390e-02],
           [7.25522481e-01, 4.39332154e-01, 2.45309879e-02],
           [7.24213709e-01, 4.47381624e-01, 2.09345748e-02],
           [7.22765968e-01, 4.55424499e-01, 1.77932038e-02],
           [7.21178603e-01, 4.63460614e-01, 1.51139005e-02],
           [7.19450034e-01, 4.71490385e-01, 1.29034121e-02],
           [7.17578728e-01, 4.79514093e-01, 1.11696237e-02],
           [7.15563473e-01, 4.87531726e-01, 9.92167759e-03],
           [7.13402011e-01, 4.95543860e-01, 9.16835746e-03],
           [7.11093082e-01, 5.03550348e-01, 8.92024840e-03],
           [7.08633928e-01, 5.11551874e-01, 9.18715968e-03],
           [7.06022885e-01, 5.19548358e-01, 9.98055273e-03],
           [7.03256797e-01, 5.27540497e-01, 1.13112827e-02],
           [7.00333308e-01, 5.35528403e-01, 1.31914645e-02],
           [6.97248836e-01, 5.43512754e-01, 1.56330268e-02],
           [6.94000118e-01, 5.51493913e-01, 1.86488222e-02],
           [6.90583003e-01, 5.59472567e-01, 2.22519914e-02],
           [6.86993159e-01, 5.67449327e-01, 2.64564846e-02],
           [6.83225628e-01, 5.75424941e-01, 3.12769913e-02],
           [6.79274890e-01, 5.83400234e-01, 3.67291720e-02],
           [6.75134865e-01, 5.91376076e-01, 4.27509268e-02],
           [6.70798729e-01, 5.99353448e-01, 4.89123750e-02],
           [6.66258945e-01, 6.07333387e-01, 5.51549440e-02],
           [6.61507217e-01, 6.15316976e-01, 6.14667048e-02],
           [6.56534234e-01, 6.23305420e-01, 6.78401362e-02],
           [6.51329933e-01, 6.31299887e-01, 7.42711050e-02],
           [6.45883015e-01, 6.39301674e-01, 8.07581459e-02],
           [6.40181118e-01, 6.47312078e-01, 8.73019542e-02],
           [6.34210936e-01, 6.55332309e-01, 9.39049938e-02],
           [6.27956874e-01, 6.63363935e-01, 1.00571400e-01],
           [6.21403808e-01, 6.71407803e-01, 1.07306437e-01],
           [6.14531776e-01, 6.79465883e-01, 1.14117128e-01],
           [6.07322678e-01, 6.87538811e-01, 1.21011150e-01],
           [5.99754661e-01, 6.95627797e-01, 1.27997639e-01],
           [5.91801878e-01, 7.03734509e-01, 1.35087294e-01],
           [5.83439746e-01, 7.11859307e-01, 1.42291328e-01],
           [5.74638962e-01, 7.20003042e-01, 1.49622601e-01],
           [5.65366923e-01, 7.28166424e-01, 1.57095387e-01],
           [5.55586040e-01, 7.36350308e-01, 1.64725785e-01],
           [5.45257929e-01, 7.44554359e-01, 1.72530767e-01],
           [5.34337843e-01, 7.52778386e-01, 1.80529474e-01],
           [5.22775708e-01, 7.61021762e-01, 1.88743035e-01],
           [5.10515333e-01, 7.69283312e-01, 1.97194796e-01],
           [4.97493503e-01, 7.77561172e-01, 2.05910588e-01],
           [4.83634506e-01, 7.85853509e-01, 2.14920226e-01],
           [4.68859095e-01, 7.94156075e-01, 2.24255120e-01],
           [4.53075331e-01, 8.02463650e-01, 2.33950671e-01],
           [4.36166044e-01, 8.10771415e-01, 2.44049843e-01],
           [4.18014515e-01, 8.19069364e-01, 2.54595740e-01],
           [3.98466974e-01, 8.27347769e-01, 2.65642088e-01],
           [3.77353041e-01, 8.35592127e-01, 2.77246960e-01],
           [3.54474232e-01, 8.43783445e-01, 2.89475347e-01],
           [3.29594196e-01, 8.51897475e-01, 3.02400858e-01],
           [3.02434518e-01, 8.59902648e-01, 3.16105006e-01],
           [2.72692702e-01, 8.67755914e-01, 3.30668567e-01],
           [2.40014665e-01, 8.75403442e-01, 3.46175030e-01],
           [2.04032200e-01, 8.82776128e-01, 3.62692416e-01],
           [1.64415609e-01, 8.89788886e-01, 3.80250268e-01],
           [1.20980526e-01, 8.96345124e-01, 3.98810670e-01],
           [7.40277319e-02, 9.02348679e-01, 4.18240542e-01],
           [2.77588786e-02, 9.07722788e-01, 4.38293044e-01],
           [1.27789185e-02, 9.12431752e-01, 4.58635213e-01],
           [3.93179496e-02, 9.16491048e-01, 4.78922144e-01],
           [8.71928025e-02, 9.19959629e-01, 4.98858624e-01],
           [1.33328898e-01, 9.22920417e-01, 5.18244914e-01],
           [1.76375421e-01, 9.25461393e-01, 5.36972167e-01],
           [2.16411634e-01, 9.27663530e-01, 5.55001352e-01],
           [2.53735141e-01, 9.29595772e-01, 5.72338103e-01],
           [2.88652031e-01, 9.31315764e-01, 5.89007926e-01],
           [3.21458374e-01, 9.32868470e-01, 6.05054746e-01],
           [3.52396293e-01, 9.34291956e-01, 6.20518400e-01],
           [3.81685935e-01, 9.35615479e-01, 6.35444286e-01],
           [4.09520082e-01, 9.36861748e-01, 6.49877377e-01],
           [4.36030520e-01, 9.38054767e-01, 6.63844355e-01],
           [4.61372763e-01, 9.39207375e-01, 6.77389198e-01],
           [4.85657570e-01, 9.40333925e-01, 6.90541118e-01],
           [5.08980779e-01, 9.41446605e-01, 7.03326643e-01],
           [5.31428755e-01, 9.42555183e-01, 7.15771194e-01],
           [5.53079254e-01, 9.43667430e-01, 7.27898804e-01],
           [5.73998300e-01, 9.44790449e-01, 7.39730200e-01],
           [5.94227037e-01, 9.45934675e-01, 7.51276523e-01],
           [6.13843594e-01, 9.47098972e-01, 7.62566752e-01],
           [6.32863755e-01, 9.48295861e-01, 7.73602965e-01],
           [6.51353569e-01, 9.49522980e-01, 7.84410542e-01],
           [6.69333275e-01, 9.50788565e-01, 7.94995073e-01],
           [6.86835680e-01, 9.52096200e-01, 8.05368319e-01],
           [7.03896821e-01, 9.53447167e-01, 8.15543888e-01],
           [7.20540733e-01, 9.54845112e-01, 8.25530415e-01],
           [7.36789782e-01, 9.56293264e-01, 8.35336084e-01],
           [7.52664767e-01, 9.57794492e-01, 8.44968614e-01],
           [7.68185007e-01, 9.59351368e-01, 8.54435231e-01],
           [7.83368427e-01, 9.60966214e-01, 8.63742657e-01],
           [7.98231621e-01, 9.62641157e-01, 8.72897087e-01],
           [8.12789913e-01, 9.64378176e-01, 8.81904158e-01],
           [8.27057406e-01, 9.66179153e-01, 8.90768921e-01],
           [8.41047005e-01, 9.68045921e-01, 8.99495786e-01],
           [8.54767774e-01, 9.69981318e-01, 9.08087374e-01],
           [8.68222635e-01, 9.71990189e-01, 9.16543559e-01],
           [8.81430468e-01, 9.74071084e-01, 9.24870307e-01],
           [8.94399475e-01, 9.76226231e-01, 9.33068602e-01],
           [9.07123054e-01, 9.78463482e-01, 9.41132913e-01],
           [9.19616588e-01, 9.80782027e-01, 9.49065298e-01],
           [9.31882459e-01, 9.83186045e-01, 9.56861211e-01],
           [9.43909764e-01, 9.85685186e-01, 9.64509322e-01],
           [9.55708766e-01, 9.88280740e-01, 9.72003341e-01],
           [9.67250754e-01, 9.90990257e-01, 9.79320134e-01],
           [9.78527005e-01, 9.93823530e-01, 9.86441171e-01],
           [9.89471812e-01, 9.96813902e-01, 9.93334732e-01],
           [1.00000000e+00, 1.00000000e+00, 1.00000000e+00]]

cmap = ListedColormap(cm_data, name="chroma")
