import streamlit as st

st.set_page_config(page_title="CropSynq | Intelligent Packaging", page_icon="🌱", layout="wide")

st.markdown("""
<style>
.main { background:#f4faf5; }
.block-container { padding-top:2rem; }
.hero { background:linear-gradient(135deg,#e2f6e7,#f8fff9); padding:35px; border-radius:22px; border:1px solid #ccebd4; margin-bottom:25px; }
.hero h1 { color:#123d25; font-size:42px; margin-bottom:5px; }
.hero p { color:#486653; font-size:18px; }
.card,.spec { background:white; padding:22px; border-radius:18px; border:1px solid #e1ebe3; box-shadow:0 4px 15px rgba(0,0,0,.05); margin-bottom:15px; }
.result { background:#f8fff9; border:2px solid #b9dfc2; padding:28px; border-radius:20px; margin-top:25px; }
.tag { display:inline-block; padding:7px 12px; margin:4px; border-radius:20px; background:#e8f6ec; color:#246238; font-size:14px; }
.benefit { background:#f7fcf8; padding:20px; border-radius:15px; border-left:5px solid #55a66a; margin-top:10px; }
.flow { background:#f8fff9; padding:16px; border-radius:14px; border:1px solid #d7eadb; text-align:center; margin-bottom:10px; }
</style>
""", unsafe_allow_html=True)


# ---------------- MULTILINGUAL UI ----------------
LANG = {
'English': {
    'sidebar': '⚙️ SIH Packaging Inputs',
    'language': '🌐 Language',
    'farmer': 'Farmer',
    'seller': 'Seller',
    'engine': 'AI Recommendation Engine',
    'farmer_intro': 'Get a practical packaging recommendation before sending produce to market.',
    'seller_intro': 'Compare packaging needs using storage, transport and product conditions.',
    'engine_intro': 'Matches food properties and environmental conditions with a packaging knowledge base.',
    'generate': '🔍 Generate AI Recommendation',
    'result': '📦 Intelligent Packaging Recommendation',
    'result_desc': 'Recommendation generated from the selected food and environmental parameters.',
    'analyzed': '🔬 Analyzed Food & Environment Properties',
    'specs': '📋 SIH Packaging Specifications',
    'insights': '💡 Practical Packaging Insights',
    'match': '📊 Recommendation Match',
    'benefits': '👨\u200d🌾 Farmer & 🏪 Seller Benefits',
    'flow': '🧠 Explainable AI Decision Flow',
    'sustain': '🌱 Sustainability & Food-Waste Impact',
    'what': 'What this upgraded prototype demonstrates',
    'enter': '👉 Enter the SIH packaging parameters in the sidebar and click **Generate AI Recommendation**.',
    'note': 'Prototype note: this is a rule-based decision-support demonstration. OTR/WVTR, MAP gas composition, shelf-life prediction and material compatibility should be validated using laboratory data, standards and packaging experts before commercial deployment.',
    'cost_note': '*Cost is an illustrative prototype estimate and changes with commodity, packaging type, transport distance and protection priority. Replace with verified local supplier quotations before real-world use.',
    'storage': '🌡️ Storage Type',
    'temperature': '🌡️ Storage Temperature (°C)',
    'humidity': '💧 Relative Humidity (%)',
    'moisture': '💦 Food Moisture Content',
    'oil': '🫒 Oil/Fat Content',
    'ph': '🧪 pH',
    'respiration': '🫁 Respiration Rate',
    'shelf': '⏳ Desired Shelf Life (days)',
    'transport': '🚚 Transportation',
    'priority': '🎯 Main Priority',
    'commodity': '🥬 Commodity',
    'material': 'Recommended Material',
    'structure': 'Packaging Structure',
    'otr': 'Oxygen Transmission Requirement (OTR)',
    'wvtr': 'Water Vapor Transmission Requirement (WVTR)',
    'thickness': 'Film/Board Thickness',
    'sealability': 'Sealability',
    'gas': 'Gas Permeability',
    'strength': 'Mechanical Strength',
    'map': 'MAP Suitability',
    'ventilation': 'Ventilation Requirement',
    'cost': 'Estimated Cost',
    'capacity': 'Capacity',
    'sustainability': 'Sustainability',
    'score': 'Recommendation Match',
    'vent_need': 'Ventilation Need',
    'damage': 'Damage Sensitivity',
    'transport_tag': 'Transport',
    'shelf_tag': 'Shelf life',
    'priority_tag': 'Priority',
    'storage_tag': 'Storage',
},
'తెలుగు': {
    'sidebar': '⚙️ SIH ప్యాకేజింగ్ ఇన్\u200cపుట్స్',
    'language': '🌐 భాష',
    'farmer': 'రైతు',
    'seller': 'విక్రేత',
    'engine': 'AI సిఫార్సు ఇంజిన్',
    'farmer_intro': 'మార్కెట్\u200cకు పంట పంపే ముందు ఉపయోగకరమైన ప్యాకేజింగ్ సిఫార్సు పొందండి.',
    'seller_intro': 'నిల్వ, రవాణా మరియు ఉత్పత్తి పరిస్థితుల ఆధారంగా ప్యాకేజింగ్ అవసరాలను పోల్చండి.',
    'engine_intro': 'ఆహార లక్షణాలు మరియు పర్యావరణ పరిస్థితులను ప్యాకేజింగ్ జ్ఞాన ఆధారంతో సరిపోలుస్తుంది.',
    'generate': '🔍 AI సిఫార్సు రూపొందించండి',
    'result': '📦 తెలివైన ప్యాకేజింగ్ సిఫార్సు',
    'result_desc': 'ఎంచుకున్న ఆహార మరియు పర్యావరణ పారామీటర్ల ఆధారంగా సిఫార్సు రూపొందించబడింది.',
    'analyzed': '🔬 విశ్లేషించిన ఆహార & పర్యావరణ లక్షణాలు',
    'specs': '📋 SIH ప్యాకేజింగ్ స్పెసిఫికేషన్స్',
    'insights': '💡 ఉపయోగకరమైన ప్యాకేజింగ్ సమాచారం',
    'match': '📊 సిఫార్సు సరిపోలిక',
    'benefits': '👨\u200d🌾 రైతు & 🏪 విక్రేత ప్రయోజనాలు',
    'flow': '🧠 వివరించగల AI నిర్ణయ విధానం',
    'sustain': '🌱 స్థిరత్వం & ఆహార వృథా ప్రభావం',
    'what': 'ఈ అప్\u200cగ్రేడ్ చేసిన ప్రోటోటైప్ ఏమి చూపిస్తుంది',
    'enter': '👉 ఎడమవైపు SIH ప్యాకేజింగ్ వివరాలను నమోదు చేసి **AI సిఫార్సు రూపొందించండి** క్లిక్ చేయండి.',
    'note': 'ప్రోటోటైప్ గమనిక: ఇది నియమాల ఆధారిత నిర్ణయ సహాయక డెమో. OTR/WVTR, MAP గ్యాస్ కూర్పు, షెల్ఫ్-లైఫ్ అంచనా మరియు మెటీరియల్ అనుకూలతను వాణిజ్య వినియోగానికి ముందు ల్యాబ్ డేటా, ప్రమాణాలు మరియు ప్యాకేజింగ్ నిపుణులతో ధృవీకరించాలి.',
    'cost_note': '*ఖర్చు ప్రోటోటైప్ అంచనా మాత్రమే. ఇది ఉత్పత్తి, ప్యాకేజింగ్ రకం, రవాణా దూరం మరియు రక్షణ అవసరాన్ని బట్టి మారుతుంది. వాస్తవ వినియోగానికి స్థానిక సరఫరాదారుల ధృవీకరించిన ధరలను ఉపయోగించండి.',
    'storage': '🌡️ నిల్వ రకం',
    'temperature': '🌡️ నిల్వ ఉష్ణోగ్రత (°C)',
    'humidity': '💧 సాపేక్ష ఆర్ద్రత (%)',
    'moisture': '💦 ఆహార తేమ',
    'oil': '🫒 నూనె/కొవ్వు శాతం',
    'ph': '🧪 pH',
    'respiration': '🫁 శ్వాసక్రియ రేటు',
    'shelf': '⏳ కావలసిన షెల్ఫ్ లైఫ్ (రోజులు)',
    'transport': '🚚 రవాణా',
    'priority': '🎯 ప్రధాన ప్రాధాన్యత',
    'commodity': '🥬 పంట / ఆహార పదార్థం',
    'material': 'సిఫార్సు చేసిన మెటీరియల్',
    'structure': 'ప్యాకేజింగ్ నిర్మాణం',
    'otr': 'ఆక్సిజన్ ట్రాన్స్\u200cమిషన్ అవసరం (OTR)',
    'wvtr': 'నీటి ఆవిరి ట్రాన్స్\u200cమిషన్ అవసరం (WVTR)',
    'thickness': 'ఫిల్మ్/బోర్డు మందం',
    'sealability': 'సీలింగ్ సామర్థ్యం',
    'gas': 'గ్యాస్ పారగమ్యత',
    'strength': 'యాంత్రిక బలం',
    'map': 'MAP అనుకూలత',
    'ventilation': 'వెంటిలేషన్ అవసరం',
    'cost': 'అంచనా ఖర్చు',
    'capacity': 'సామర్థ్యం',
    'sustainability': 'స్థిరత్వం',
    'score': 'సిఫార్సు సరిపోలిక',
    'vent_need': 'వెంటిలేషన్ అవసరం',
    'damage': 'నష్టం పట్ల సున్నితత్వం',
    'transport_tag': 'రవాణా',
    'shelf_tag': 'షెల్ఫ్ లైఫ్',
    'priority_tag': 'ప్రాధాన్యత',
    'storage_tag': 'నిల్వ',
},
'हिन्दी': {
    'sidebar': '⚙️ SIH पैकेजिंग इनपुट',
    'language': '🌐 भाषा',
    'farmer': 'किसान',
    'seller': 'विक्रेता',
    'engine': 'AI सिफारिश इंजन',
    'farmer_intro': 'बाजार भेजने से पहले उपज के लिए व्यावहारिक पैकेजिंग सुझाव प्राप्त करें।',
    'seller_intro': 'भंडारण, परिवहन और उत्पाद की स्थितियों के आधार पर पैकेजिंग जरूरतों की तुलना करें।',
    'engine_intro': 'खाद्य गुणों और पर्यावरणीय स्थितियों को पैकेजिंग ज्ञान आधार से मिलाता है।',
    'generate': '🔍 AI सिफारिश बनाएं',
    'result': '📦 बुद्धिमान पैकेजिंग सिफारिश',
    'result_desc': 'चयनित खाद्य और पर्यावरणीय मापदंडों से सिफारिश तैयार की गई है।',
    'analyzed': '🔬 विश्लेषित खाद्य एवं पर्यावरण गुण',
    'specs': '📋 SIH पैकेजिंग विनिर्देश',
    'insights': '💡 व्यावहारिक पैकेजिंग जानकारी',
    'match': '📊 सिफारिश मिलान',
    'benefits': '👨\u200d🌾 किसान एवं 🏪 विक्रेता लाभ',
    'flow': '🧠 समझने योग्य AI निर्णय प्रक्रिया',
    'sustain': '🌱 स्थिरता एवं खाद्य अपशिष्ट प्रभाव',
    'what': 'यह उन्नत प्रोटोटाइप क्या दिखाता है',
    'enter': '👉 साइडबार में SIH पैकेजिंग मापदंड भरें और **AI सिफारिश बनाएं** पर क्लिक करें।',
    'note': 'प्रोटोटाइप नोट: यह नियम-आधारित निर्णय-सहायता डेमो है। व्यावसायिक उपयोग से पहले OTR/WVTR, MAP गैस संरचना, शेल्फ-लाइफ और सामग्री अनुकूलता को प्रयोगशाला डेटा, मानकों और विशेषज्ञों से सत्यापित करें।',
    'cost_note': '*लागत केवल प्रोटोटाइप अनुमान है और उपज, पैकेजिंग प्रकार, दूरी तथा सुरक्षा प्राथमिकता के अनुसार बदलती है। वास्तविक उपयोग से पहले स्थानीय आपूर्तिकर्ता की कीमत सत्यापित करें।',
    'storage': '🌡️ भंडारण प्रकार',
    'temperature': '🌡️ भंडारण तापमान (°C)',
    'humidity': '💧 सापेक्ष आर्द्रता (%)',
    'moisture': '💦 खाद्य नमी',
    'oil': '🫒 तेल/वसा सामग्री',
    'ph': '🧪 pH',
    'respiration': '🫁 श्वसन दर',
    'shelf': '⏳ वांछित शेल्फ लाइफ (दिन)',
    'transport': '🚚 परिवहन',
    'priority': '🎯 मुख्य प्राथमिकता',
    'commodity': '🥬 फसल / खाद्य पदार्थ',
    'material': 'अनुशंसित सामग्री',
    'structure': 'पैकेजिंग संरचना',
    'otr': 'ऑक्सीजन ट्रांसमिशन आवश्यकता (OTR)',
    'wvtr': 'जल वाष्प ट्रांसमिशन आवश्यकता (WVTR)',
    'thickness': 'फिल्म/बोर्ड मोटाई',
    'sealability': 'सीलिंग क्षमता',
    'gas': 'गैस पारगम्यता',
    'strength': 'यांत्रिक मजबूती',
    'map': 'MAP उपयुक्तता',
    'ventilation': 'वेंटिलेशन आवश्यकता',
    'cost': 'अनुमानित लागत',
    'capacity': 'क्षमता',
    'sustainability': 'स्थिरता',
    'score': 'सिफारिश मिलान',
    'vent_need': 'वेंटिलेशन आवश्यकता',
    'damage': 'क्षति संवेदनशीलता',
    'transport_tag': 'परिवहन',
    'shelf_tag': 'शेल्फ लाइफ',
    'priority_tag': 'प्राथमिकता',
    'storage_tag': 'भंडारण',
},
'தமிழ்': {
    'sidebar': '⚙️ SIH பேக்கேஜிங் உள்ளீடுகள்',
    'language': '🌐 மொழி',
    'farmer': 'விவசாயி',
    'seller': 'விற்பனையாளர்',
    'engine': 'AI பரிந்துரை இயந்திரம்',
    'farmer_intro': 'சந்தைக்கு அனுப்பும் முன் விளைபொருளுக்கான நடைமுறை பேக்கேஜிங் பரிந்துரையைப் பெறுங்கள்.',
    'seller_intro': 'சேமிப்பு, போக்குவரத்து மற்றும் பொருள் நிலைகளை வைத்து பேக்கேஜிங் தேவைகளை ஒப்பிடுங்கள்.',
    'engine_intro': 'உணவு பண்புகள் மற்றும் சூழல் நிலைகளை பேக்கேஜிங் அறிவுத் தளத்துடன் பொருத்துகிறது.',
    'generate': '🔍 AI பரிந்துரையை உருவாக்கு',
    'result': '📦 புத்திசாலி பேக்கேஜிங் பரிந்துரை',
    'result_desc': 'தேர்ந்தெடுத்த உணவு மற்றும் சூழல் அளவுருக்களின் அடிப்படையில் பரிந்துரை உருவாக்கப்பட்டது.',
    'analyzed': '🔬 பகுப்பாய்வு செய்யப்பட்ட உணவு & சூழல் பண்புகள்',
    'specs': '📋 SIH பேக்கேஜிங் விவரக்குறிப்புகள்',
    'insights': '💡 நடைமுறை பேக்கேஜிங் தகவல்',
    'match': '📊 பரிந்துரை பொருத்தம்',
    'benefits': '👨\u200d🌾 விவசாயி & 🏪 விற்பனையாளர் நன்மைகள்',
    'flow': '🧠 விளக்கக்கூடிய AI முடிவு நடைமுறை',
    'sustain': '🌱 நிலைத்தன்மை & உணவு வீணாக்க தாக்கம்',
    'what': 'இந்த மேம்படுத்தப்பட்ட முன்மாதிரி காட்டுவது',
    'enter': '👉 பக்கப்பட்டியில் SIH அளவுருக்களை உள்ளிட்டு **AI பரிந்துரையை உருவாக்கு** என்பதைக் கிளிக் செய்யுங்கள்.',
    'note': 'முன்மாதிரி குறிப்பு: இது விதி-அடிப்படையிலான முடிவு உதவி டெமோ. வணிக பயன்பாட்டிற்கு முன் OTR/WVTR, MAP வாயு கலவை, சேமிப்பு ஆயுள் மற்றும் பொருள் பொருத்தத்தை ஆய்வக தரவு மற்றும் நிபுணர்களால் சரிபார்க்க வேண்டும்.',
    'cost_note': '*செலவு முன்மாதிரி மதிப்பீடு மட்டுமே; பொருள், பேக்கேஜிங் வகை, போக்குவரத்து தூரம் மற்றும் பாதுகாப்பு முன்னுரிமை அடிப்படையில் மாறும்.',
    'storage': '🌡️ சேமிப்பு வகை',
    'temperature': '🌡️ சேமிப்பு வெப்பநிலை (°C)',
    'humidity': '💧 சார்பு ஈரப்பதம் (%)',
    'moisture': '💦 உணவு ஈரப்பதம்',
    'oil': '🫒 எண்ணெய்/கொழுப்பு அளவு',
    'ph': '🧪 pH',
    'respiration': '🫁 சுவாச விகிதம்',
    'shelf': '⏳ தேவையான சேமிப்பு ஆயுள் (நாட்கள்)',
    'transport': '🚚 போக்குவரத்து',
    'priority': '🎯 முக்கிய முன்னுரிமை',
    'commodity': '🥬 பயிர் / உணவு பொருள்',
    'material': 'பரிந்துரைக்கப்பட்ட பொருள்',
    'structure': 'பேக்கேஜிங் அமைப்பு',
    'otr': 'ஆக்சிஜன் பரிமாற்ற தேவை (OTR)',
    'wvtr': 'நீராவி பரிமாற்ற தேவை (WVTR)',
    'thickness': 'பிலிம்/போர்டு தடிமன்',
    'sealability': 'சீலிங் திறன்',
    'gas': 'வாயு ஊடுருவல்',
    'strength': 'இயந்திர வலிமை',
    'map': 'MAP பொருத்தம்',
    'ventilation': 'காற்றோட்ட தேவை',
    'cost': 'மதிப்பிடப்பட்ட செலவு',
    'capacity': 'திறன்',
    'sustainability': 'நிலைத்தன்மை',
    'score': 'பரிந்துரை பொருத்தம்',
    'vent_need': 'காற்றோட்ட தேவை',
    'damage': 'சேத உணர்திறன்',
    'transport_tag': 'போக்குவரத்து',
    'shelf_tag': 'சேமிப்பு ஆயுள்',
    'priority_tag': 'முன்னுரிமை',
    'storage_tag': 'சேமிப்பு',
},
'ಕನ್ನಡ': {
    'sidebar': '⚙️ SIH ಪ್ಯಾಕೇಜಿಂಗ್ ಇನ್\u200cಪುಟ್\u200cಗಳು',
    'language': '🌐 ಭಾಷೆ',
    'farmer': 'ರೈತ',
    'seller': 'ಮಾರಾಟಗಾರ',
    'engine': 'AI ಶಿಫಾರಸು ಎಂಜಿನ್',
    'farmer_intro': 'ಮಾರುಕಟ್ಟೆಗೆ ಕಳುಹಿಸುವ ಮೊದಲು ಉತ್ಪನ್ನಕ್ಕೆ ಪ್ರಾಯೋಗಿಕ ಪ್ಯಾಕೇಜಿಂಗ್ ಶಿಫಾರಸು ಪಡೆಯಿರಿ.',
    'seller_intro': 'ಸಂಗ್ರಹಣೆ, ಸಾರಿಗೆ ಮತ್ತು ಉತ್ಪನ್ನದ ಪರಿಸ್ಥಿತಿಗಳ ಆಧಾರದ ಮೇಲೆ ಪ್ಯಾಕೇಜಿಂಗ್ ಅಗತ್ಯಗಳನ್ನು ಹೋಲಿಸಿ.',
    'engine_intro': 'ಆಹಾರ ಗುಣಲಕ್ಷಣಗಳು ಮತ್ತು ಪರಿಸರ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಪ್ಯಾಕೇಜಿಂಗ್ ಜ್ಞಾನ ಆಧಾರದೊಂದಿಗೆ ಹೊಂದಿಸುತ್ತದೆ.',
    'generate': '🔍 AI ಶಿಫಾರಸು ರಚಿಸಿ',
    'result': '📦 ಬುದ್ಧಿವಂತ ಪ್ಯಾಕೇಜಿಂಗ್ ಶಿಫಾರಸು',
    'result_desc': 'ಆಯ್ಕೆ ಮಾಡಿದ ಆಹಾರ ಮತ್ತು ಪರಿಸರ ನಿಯತಾಂಕಗಳ ಆಧಾರದ ಮೇಲೆ ಶಿಫಾರಸು ಸಿದ್ಧವಾಗಿದೆ.',
    'analyzed': '🔬 ವಿಶ್ಲೇಷಿಸಿದ ಆಹಾರ & ಪರಿಸರ ಗುಣಲಕ್ಷಣಗಳು',
    'specs': '📋 SIH ಪ್ಯಾಕೇಜಿಂಗ್ ವಿಶೇಷಣಗಳು',
    'insights': '💡 ಪ್ರಾಯೋಗಿಕ ಪ್ಯಾಕೇಜಿಂಗ್ ಮಾಹಿತಿ',
    'match': '📊 ಶಿಫಾರಸು ಹೊಂದಾಣಿಕೆ',
    'benefits': '👨\u200d🌾 ರೈತ & 🏪 ಮಾರಾಟಗಾರರ ಪ್ರಯೋಜನಗಳು',
    'flow': '🧠 ವಿವರಿಸಬಹುದಾದ AI ನಿರ್ಧಾರ ವಿಧಾನ',
    'sustain': '🌱 ಸ್ಥಿರತೆ & ಆಹಾರ ವ್ಯರ್ಥದ ಪರಿಣಾಮ',
    'what': 'ಈ ಅಪ್\u200cಗ್ರೇಡ್ ಮಾಡಿದ ಪ್ರೋಟೋಟೈಪ್ ತೋರಿಸುವುದು',
    'enter': '👉 ಸೈಡ್\u200cಬಾರ್\u200cನಲ್ಲಿ SIH ಪ್ಯಾಕೇಜಿಂಗ್ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ ಮತ್ತು **AI ಶಿಫಾರಸು ರಚಿಸಿ** ಕ್ಲಿಕ್ ಮಾಡಿ.',
    'note': 'ಪ್ರೋಟೋಟೈಪ್ ಸೂಚನೆ: ಇದು ನಿಯಮ ಆಧಾರಿತ ನಿರ್ಧಾರ ಸಹಾಯ ಡೆಮೋ. ವಾಣಿಜ್ಯ ಬಳಕೆಗೆ ಮೊದಲು OTR/WVTR, MAP ಅನಿಲ ಸಂಯೋಜನೆ, ಶೆಲ್ಫ್-ಲೈಫ್ ಮತ್ತು ವಸ್ತು ಹೊಂದಾಣಿಕೆಯನ್ನು ಪ್ರಯೋಗಾಲಯದ ಡೇಟಾ, ಮಾನದಂಡಗಳು ಮತ್ತು ತಜ್ಞರಿಂದ ಪರಿಶೀಲಿಸಬೇಕು.',
    'cost_note': '*ವೆಚ್ಚವು ಪ್ರೋಟೋಟೈಪ್ ಅಂದಾಜು ಮಾತ್ರ; ಉತ್ಪನ್ನ, ಪ್ಯಾಕೇಜಿಂಗ್ ಪ್ರಕಾರ, ಸಾರಿಗೆ ದೂರ ಮತ್ತು ರಕ್ಷಣಾ ಆದ್ಯತೆಯಿಂದ ಬದಲಾಗುತ್ತದೆ.',
    'storage': '🌡️ ಸಂಗ್ರಹಣೆಯ ಪ್ರಕಾರ',
    'temperature': '🌡️ ಸಂಗ್ರಹಣೆಯ ತಾಪಮಾನ (°C)',
    'humidity': '💧 ಸಾಪೇಕ್ಷ ಆರ್ದ್ರತೆ (%)',
    'moisture': '💦 ಆಹಾರದ ತೇವಾಂಶ',
    'oil': '🫒 ಎಣ್ಣೆ/ಕೊಬ್ಬಿನ ಪ್ರಮಾಣ',
    'ph': '🧪 pH',
    'respiration': '🫁 ಉಸಿರಾಟ ದರ',
    'shelf': '⏳ ಬೇಕಾದ ಶೆಲ್ಫ್ ಲೈಫ್ (ದಿನಗಳು)',
    'transport': '🚚 ಸಾರಿಗೆ',
    'priority': '🎯 ಮುಖ್ಯ ಆದ್ಯತೆ',
    'commodity': '🥬 ಬೆಳೆ / ಆಹಾರ ಪದಾರ್ಥ',
    'material': 'ಶಿಫಾರಸು ಮಾಡಿದ ವಸ್ತು',
    'structure': 'ಪ್ಯಾಕೇಜಿಂಗ್ ರಚನೆ',
    'otr': 'ಆಮ್ಲಜನಕ ಪ್ರಸರಣ ಅಗತ್ಯ (OTR)',
    'wvtr': 'ನೀರಿನ ಆವಿ ಪ್ರಸರಣ ಅಗತ್ಯ (WVTR)',
    'thickness': 'ಫಿಲ್ಮ್/ಬೋರ್ಡ್ ದಪ್ಪ',
    'sealability': 'ಸೀಲಿಂಗ್ ಸಾಮರ್ಥ್ಯ',
    'gas': 'ಅನಿಲ ಪ್ರವೇಶ',
    'strength': 'ಯಾಂತ್ರಿಕ ಬಲ',
    'map': 'MAP ಸೂಕ್ತತೆ',
    'ventilation': 'ವಾತಾಯನ ಅಗತ್ಯ',
    'cost': 'ಅಂದಾಜು ವೆಚ್ಚ',
    'capacity': 'ಸಾಮರ್ಥ್ಯ',
    'sustainability': 'ಸ್ಥಿರತೆ',
    'score': 'ಶಿಫಾರಸು ಹೊಂದಾಣಿಕೆ',
    'vent_need': 'ವಾತಾಯನ ಅಗತ್ಯ',
    'damage': 'ಹಾನಿ ಸಂವೇದನೆ',
    'transport_tag': 'ಸಾರಿಗೆ',
    'shelf_tag': 'ಶೆಲ್ಫ್ ಲೈಫ್',
    'priority_tag': 'ಆದ್ಯತೆ',
    'storage_tag': 'ಸಂಗ್ರಹಣೆ',
},
'മലയാളം': {
    'sidebar': '⚙️ SIH പാക്കേജിംഗ് ഇൻപുട്ടുകൾ',
    'language': '🌐 ഭാഷ',
    'farmer': 'കർഷകൻ',
    'seller': 'വിൽപ്പനക്കാരൻ',
    'engine': 'AI ശുപാർശ എഞ്ചിൻ',
    'farmer_intro': 'വിപണിയിലേക്ക് അയയ്ക്കുന്നതിന് മുമ്പ് വിളയ്ക്ക് പ്രായോഗിക പാക്കേജിംഗ് ശുപാർശ നേടുക.',
    'seller_intro': 'സംഭരണം, ഗതാഗതം, ഉൽപ്പന്ന സാഹചര്യങ്ങൾ എന്നിവ അടിസ്ഥാനമാക്കി പാക്കേജിംഗ് ആവശ്യങ്ങൾ താരതമ്യം ചെയ്യുക.',
    'engine_intro': 'ഭക്ഷ്യ ഗുണങ്ങളും പരിസ്ഥിതി സാഹചര്യങ്ങളും പാക്കേജിംഗ് അറിവ് അടിസ്ഥാനവുമായി പൊരുത്തപ്പെടുത്തുന്നു.',
    'generate': '🔍 AI ശുപാർശ സൃഷ്ടിക്കുക',
    'result': '📦 ബുദ്ധിമാനായ പാക്കേജിംഗ് ശുപാർശ',
    'result_desc': 'തിരഞ്ഞെടുത്ത ഭക്ഷണ-പരിസ്ഥിതി പാരാമീറ്ററുകളുടെ അടിസ്ഥാനത്തിൽ ശുപാർശ സൃഷ്ടിച്ചു.',
    'analyzed': '🔬 വിശകലനം ചെയ്ത ഭക്ഷ്യ & പരിസ്ഥിതി ഗുണങ്ങൾ',
    'specs': '📋 SIH പാക്കേജിംഗ് സവിശേഷതകൾ',
    'insights': '💡 പ്രായോഗിക പാക്കേജിംഗ് വിവരം',
    'match': '📊 ശുപാർശ പൊരുത്തം',
    'benefits': '👨\u200d🌾 കർഷക & 🏪 വിൽപ്പനക്കാരൻ നേട്ടങ്ങൾ',
    'flow': '🧠 വിശദീകരിക്കാവുന്ന AI തീരുമാന പ്രക്രിയ',
    'sustain': '🌱 സുസ്ഥിരത & ഭക്ഷ്യ മാലിന്യ സ്വാധീനം',
    'what': 'ഈ അപ്\u200cഗ്രേഡ് ചെയ്ത പ്രോട്ടോടൈപ്പ് കാണിക്കുന്നത്',
    'enter': '👉 സൈഡ്\u200cബാറിൽ SIH പാക്കേജിംഗ് പാരാമീറ്ററുകൾ നൽകി **AI ശുപാർശ സൃഷ്ടിക്കുക** ക്ലിക്ക് ചെയ്യുക.',
    'note': 'പ്രോട്ടോടൈപ്പ് കുറിപ്പ്: ഇത് നിയമാധിഷ്ഠിത തീരുമാന സഹായ ഡെമോയാണ്. വാണിജ്യ ഉപയോഗത്തിന് മുമ്പ് OTR/WVTR, MAP വാതക ഘടന, ഷെൽഫ് ലൈഫ്, മെറ്റീരിയൽ അനുയോജ്യത എന്നിവ ലാബ് ഡാറ്റയും വിദഗ്ധരും ഉപയോഗിച്ച് പരിശോധിക്കണം.',
    'cost_note': '*ചെലവ് പ്രോട്ടോടൈപ്പ് കണക്കുകൂട്ടൽ മാത്രമാണ്; ഉൽപ്പന്നം, പാക്കേജിംഗ് തരം, ഗതാഗത ദൂരം, സംരക്ഷണ മുൻഗണന എന്നിവ അനുസരിച്ച് മാറും.',
    'storage': '🌡️ സംഭരണ തരം',
    'temperature': '🌡️ സംഭരണ താപനില (°C)',
    'humidity': '💧 ആപേക്ഷിക ആർദ്രത (%)',
    'moisture': '💦 ഭക്ഷ്യ ഈർപ്പം',
    'oil': '🫒 എണ്ണ/കൊഴുപ്പ് അളവ്',
    'ph': '🧪 pH',
    'respiration': '🫁 ശ്വസന നിരക്ക്',
    'shelf': '⏳ ആവശ്യമായ ഷെൽഫ് ലൈഫ് (ദിവസങ്ങൾ)',
    'transport': '🚚 ഗതാഗതം',
    'priority': '🎯 പ്രധാന മുൻഗണന',
    'commodity': '🥬 വിള / ഭക്ഷ്യവസ്തു',
    'material': 'ശുപാർശ ചെയ്ത മെറ്റീരിയൽ',
    'structure': 'പാക്കേജിംഗ് ഘടന',
    'otr': 'ഓക്സിജൻ ട്രാൻസ്മിഷൻ ആവശ്യം (OTR)',
    'wvtr': 'ജലവാഷ്പ ട്രാൻസ്മിഷൻ ആവശ്യം (WVTR)',
    'thickness': 'ഫിലിം/ബോർഡ് കനം',
    'sealability': 'സീലിംഗ് കഴിവ്',
    'gas': 'വാതക പ്രവേശനക്ഷമത',
    'strength': 'യാന്ത്രിക ശക്തി',
    'map': 'MAP അനുയോജ്യത',
    'ventilation': 'വായുസഞ്ചാര ആവശ്യം',
    'cost': 'അനുമാനിച്ച ചെലവ്',
    'capacity': 'ശേഷി',
    'sustainability': 'സുസ്ഥിരത',
    'score': 'ശുപാർശ പൊരുത്തം',
    'vent_need': 'വായുസഞ്ചാര ആവശ്യം',
    'damage': 'നാശസാധ്യത',
    'transport_tag': 'ഗതാഗതം',
    'shelf_tag': 'ഷെൽഫ് ലൈഫ്',
    'priority_tag': 'മുൻഗണന',
    'storage_tag': 'സംഭരണം',
},
'Marathi': {
    'sidebar': '⚙️ SIH पॅकेजिंग इनपुट्स',
    'language': '🌐 भाषा',
    'farmer': 'शेतकरी',
    'seller': 'विक्रेता',
    'engine': 'AI शिफारस इंजिन',
    'farmer_intro': 'बाजारात पाठवण्यापूर्वी उत्पादनासाठी व्यावहारिक पॅकेजिंग शिफारस मिळवा.',
    'seller_intro': 'साठवण, वाहतूक आणि उत्पादनाच्या परिस्थितीनुसार पॅकेजिंग गरजांची तुलना करा.',
    'engine_intro': 'अन्नाचे गुणधर्म आणि पर्यावरणीय परिस्थिती पॅकेजिंग ज्ञानाधाराशी जुळवते.',
    'generate': '🔍 AI शिफारस तयार करा',
    'result': '📦 बुद्धिमान पॅकेजिंग शिफारस',
    'result_desc': 'निवडलेल्या अन्न व पर्यावरणीय मापदंडांवर आधारित शिफारस तयार केली आहे.',
    'analyzed': '🔬 विश्लेषित अन्न व पर्यावरण गुणधर्म',
    'specs': '📋 SIH पॅकेजिंग तपशील',
    'insights': '💡 व्यावहारिक पॅकेजिंग माहिती',
    'match': '📊 शिफारस जुळणी',
    'benefits': '👨\u200d🌾 शेतकरी व 🏪 विक्रेता फायदे',
    'flow': '🧠 समजण्याजोगी AI निर्णय प्रक्रिया',
    'sustain': '🌱 टिकाऊपणा व अन्न अपव्यय परिणाम',
    'what': 'हे अपग्रेड केलेले प्रोटोटाइप काय दाखवते',
    'enter': '👉 साइडबारमध्ये SIH पॅकेजिंग मापदंड भरा आणि **AI शिफारस तयार करा** क्लिक करा.',
    'note': 'प्रोटोटाइप सूचना: हे नियम-आधारित निर्णय सहाय्य डेमो आहे. व्यावसायिक वापरापूर्वी OTR/WVTR, MAP वायू रचना, शेल्फ लाइफ आणि सामग्री सुसंगतता प्रयोगशाळा डेटा व तज्ज्ञांकडून तपासा.',
    'cost_note': '*खर्च हा फक्त प्रोटोटाइप अंदाज आहे आणि उत्पादन, पॅकेजिंग प्रकार, वाहतूक अंतर व संरक्षणाच्या प्राधान्यानुसार बदलतो.',
    'storage': '🌡️ साठवण प्रकार',
    'temperature': '🌡️ साठवण तापमान (°C)',
    'humidity': '💧 सापेक्ष आर्द्रता (%)',
    'moisture': '💦 अन्नातील ओलावा',
    'oil': '🫒 तेल/चरबीचे प्रमाण',
    'ph': '🧪 pH',
    'respiration': '🫁 श्वसन दर',
    'shelf': '⏳ अपेक्षित शेल्फ लाइफ (दिवस)',
    'transport': '🚚 वाहतूक',
    'priority': '🎯 मुख्य प्राधान्य',
    'commodity': '🥬 पीक / अन्नपदार्थ',
    'material': 'शिफारस केलेली सामग्री',
    'structure': 'पॅकेजिंग रचना',
    'otr': 'ऑक्सिजन ट्रान्समिशन आवश्यकता (OTR)',
    'wvtr': 'जलवाष्प ट्रान्समिशन आवश्यकता (WVTR)',
    'thickness': 'फिल्म/बोर्ड जाडी',
    'sealability': 'सीलिंग क्षमता',
    'gas': 'वायू पारगम्यता',
    'strength': 'यांत्रिक ताकद',
    'map': 'MAP योग्यते',
    'ventilation': 'वायुवीजन आवश्यकता',
    'cost': 'अंदाजित खर्च',
    'capacity': 'क्षमता',
    'sustainability': 'टिकाऊपणा',
    'score': 'शिफारस जुळणी',
    'vent_need': 'वायुवीजन आवश्यकता',
    'damage': 'नुकसान संवेदनशीलता',
    'transport_tag': 'वाहतूक',
    'shelf_tag': 'शेल्फ लाइफ',
    'priority_tag': 'प्राधान्य',
    'storage_tag': 'साठवण',
},
'বাংলা': {
    'sidebar': '⚙️ SIH প্যাকেজিং ইনপুট',
    'language': '🌐 ভাষা',
    'farmer': 'কৃষক',
    'seller': 'বিক্রেতা',
    'engine': 'AI সুপারিশ ইঞ্জিন',
    'farmer_intro': 'বাজারে পাঠানোর আগে উৎপাদনের জন্য ব্যবহারিক প্যাকেজিং সুপারিশ পান।',
    'seller_intro': 'সংরক্ষণ, পরিবহন এবং পণ্যের অবস্থার ভিত্তিতে প্যাকেজিংয়ের প্রয়োজন তুলনা করুন।',
    'engine_intro': 'খাদ্য বৈশিষ্ট্য ও পরিবেশগত অবস্থাকে প্যাকেজিং জ্ঞানভাণ্ডারের সঙ্গে মিলিয়ে দেয়।',
    'generate': '🔍 AI সুপারিশ তৈরি করুন',
    'result': '📦 বুদ্ধিমান প্যাকেজিং সুপারিশ',
    'result_desc': 'নির্বাচিত খাদ্য ও পরিবেশগত প্যারামিটারের ভিত্তিতে সুপারিশ তৈরি হয়েছে।',
    'analyzed': '🔬 বিশ্লেষিত খাদ্য ও পরিবেশের বৈশিষ্ট্য',
    'specs': '📋 SIH প্যাকেজিং স্পেসিফিকেশন',
    'insights': '💡 ব্যবহারিক প্যাকেজিং তথ্য',
    'match': '📊 সুপারিশ মিল',
    'benefits': '👨\u200d🌾 কৃষক ও 🏪 বিক্রেতার সুবিধা',
    'flow': '🧠 ব্যাখ্যাযোগ্য AI সিদ্ধান্ত প্রক্রিয়া',
    'sustain': '🌱 স্থায়িত্ব ও খাদ্য অপচয়ের প্রভাব',
    'what': 'এই আপগ্রেড করা প্রোটোটাইপ যা দেখায়',
    'enter': '👉 সাইডবারে SIH প্যাকেজিং প্যারামিটার দিন এবং **AI সুপারিশ তৈরি করুন** ক্লিক করুন।',
    'note': 'প্রোটোটাইপ নোট: এটি নিয়মভিত্তিক সিদ্ধান্ত সহায়তা ডেমো। বাণিজ্যিক ব্যবহারের আগে OTR/WVTR, MAP গ্যাস সংমিশ্রণ, শেলফ লাইফ ও উপাদান সামঞ্জস্য ল্যাব ডেটা ও বিশেষজ্ঞদের দিয়ে যাচাই করতে হবে।',
    'cost_note': '*খরচটি কেবল প্রোটোটাইপ অনুমান; পণ্য, প্যাকেজিং ধরন, পরিবহন দূরত্ব ও সুরক্ষা অগ্রাধিকারে পরিবর্তিত হয়।',
    'storage': '🌡️ সংরক্ষণের ধরন',
    'temperature': '🌡️ সংরক্ষণ তাপমাত্রা (°C)',
    'humidity': '💧 আপেক্ষিক আর্দ্রতা (%)',
    'moisture': '💦 খাদ্যের আর্দ্রতা',
    'oil': '🫒 তেল/চর্বির পরিমাণ',
    'ph': '🧪 pH',
    'respiration': '🫁 শ্বাস-প্রশ্বাসের হার',
    'shelf': '⏳ কাঙ্ক্ষিত শেলফ লাইফ (দিন)',
    'transport': '🚚 পরিবহন',
    'priority': '🎯 প্রধান অগ্রাধিকার',
    'commodity': '🥬 ফসল / খাদ্যপণ্য',
    'material': 'প্রস্তাবিত উপাদান',
    'structure': 'প্যাকেজিং কাঠামো',
    'otr': 'অক্সিজেন ট্রান্সমিশন প্রয়োজন (OTR)',
    'wvtr': 'জলীয় বাষ্প ট্রান্সমিশন প্রয়োজন (WVTR)',
    'thickness': 'ফিল্ম/বোর্ডের পুরুত্ব',
    'sealability': 'সিলিং ক্ষমতা',
    'gas': 'গ্যাস পারমিয়াবিলিটি',
    'strength': 'যান্ত্রিক শক্তি',
    'map': 'MAP উপযোগিতা',
    'ventilation': 'বায়ু চলাচলের প্রয়োজন',
    'cost': 'আনুমানিক খরচ',
    'capacity': 'ধারণক্ষমতা',
    'sustainability': 'স্থায়িত্ব',
    'score': 'সুপারিশ মিল',
    'vent_need': 'বায়ু চলাচলের প্রয়োজন',
    'damage': 'ক্ষতির সংবেদনশীলতা',
    'transport_tag': 'পরিবহন',
    'shelf_tag': 'শেলফ লাইফ',
    'priority_tag': 'অগ্রাধিকার',
    'storage_tag': 'সংরক্ষণ',
},
'ગુજરાતી': {
    'sidebar': '⚙️ SIH પેકેજિંગ ઇનપુટ્સ',
    'language': '🌐 ભાષા',
    'farmer': 'ખેડૂત',
    'seller': 'વેચનાર',
    'engine': 'AI ભલામણ એન્જિન',
    'farmer_intro': 'બજારમાં મોકલતા પહેલાં ઉપજ માટે વ્યવહારુ પેકેજિંગ ભલામણ મેળવો.',
    'seller_intro': 'સંગ્રહ, પરિવહન અને ઉત્પાદનની પરિસ્થિતિ પ્રમાણે પેકેજિંગ જરૂરિયાતોની તુલના કરો.',
    'engine_intro': 'ખાદ્ય ગુણધર્મો અને પર્યાવરણીય પરિસ્થિતિઓને પેકેજિંગ જ્ઞાન આધાર સાથે મેળવે છે.',
    'generate': '🔍 AI ભલામણ બનાવો',
    'result': '📦 બુદ્ધિશાળી પેકેજિંગ ભલામણ',
    'result_desc': 'પસંદ કરેલા ખાદ્ય અને પર્યાવરણીય પરિમાણોના આધારે ભલામણ તૈયાર થઈ છે.',
    'analyzed': '🔬 વિશ્લેષિત ખાદ્ય અને પર્યાવરણ ગુણધર્મો',
    'specs': '📋 SIH પેકેજિંગ વિશિષ્ટતાઓ',
    'insights': '💡 વ્યવહારુ પેકેજિંગ માહિતી',
    'match': '📊 ભલામણ મેળ',
    'benefits': '👨\u200d🌾 ખેડૂત અને 🏪 વેચનાર લાભો',
    'flow': '🧠 સમજાવી શકાય તેવી AI નિર્ણય પ્રક્રિયા',
    'sustain': '🌱 ટકાઉપણું અને ખાદ્ય બગાડ અસર',
    'what': 'આ અપગ્રેડ કરેલ પ્રોટોટાઇપ શું દર્શાવે છે',
    'enter': '👉 સાઇડબારમાં SIH પેકેજિંગ પરિમાણો દાખલ કરો અને **AI ભલામણ બનાવો** ક્લિક કરો.',
    'note': 'પ્રોટોટાઇપ નોંધ: આ નિયમ આધારિત નિર્ણય સહાય ડેમો છે. વ્યાવસાયિક ઉપયોગ પહેલાં OTR/WVTR, MAP ગેસ રચના, શેલ્ફ લાઇફ અને સામગ્રી સુસંગતતા લેબ ડેટા અને નિષ્ણાતોથી ચકાસવી જોઈએ.',
    'cost_note': '*ખર્ચ માત્ર પ્રોટોટાઇપ અંદાજ છે અને ઉત્પાદન, પેકેજિંગ પ્રકાર, પરિવહન અંતર તથા સુરક્ષા પ્રાથમિકતા પ્રમાણે બદલાય છે.',
    'storage': '🌡️ સંગ્રહ પ્રકાર',
    'temperature': '🌡️ સંગ્રહ તાપમાન (°C)',
    'humidity': '💧 સાપેક્ષ ભેજ (%)',
    'moisture': '💦 ખાદ્ય ભેજ',
    'oil': '🫒 તેલ/ચરબીનું પ્રમાણ',
    'ph': '🧪 pH',
    'respiration': '🫁 શ્વસન દર',
    'shelf': '⏳ ઇચ્છિત શેલ્ફ લાઇફ (દિવસ)',
    'transport': '🚚 પરિવહન',
    'priority': '🎯 મુખ્ય પ્રાથમિકતા',
    'commodity': '🥬 પાક / ખાદ્ય પદાર્થ',
    'material': 'ભલામણ કરેલ સામગ્રી',
    'structure': 'પેકેજિંગ રચના',
    'otr': 'ઓક્સિજન ટ્રાન્સમિશન જરૂરિયાત (OTR)',
    'wvtr': 'જળવાષ્પ ટ્રાન્સમિશન જરૂરિયાત (WVTR)',
    'thickness': 'ફિલ્મ/બોર્ડ જાડાઈ',
    'sealability': 'સીલિંગ ક્ષમતા',
    'gas': 'ગેસ પારગમ્યતા',
    'strength': 'યાંત્રિક મજબૂતી',
    'map': 'MAP યોગ્યતા',
    'ventilation': 'વેન્ટિલેશન જરૂરિયાત',
    'cost': 'અંદાજિત ખર્ચ',
    'capacity': 'ક્ષમતા',
    'sustainability': 'ટકાઉપણું',
    'score': 'ભલામણ મેળ',
    'vent_need': 'વેન્ટિલેશન જરૂરિયાત',
    'damage': 'નુકસાન સંવેદનશીલતા',
    'transport_tag': 'પરિવહન',
    'shelf_tag': 'શેલ્ફ લાઇફ',
    'priority_tag': 'પ્રાથમિકતા',
    'storage_tag': 'સંગ્રહ',
},
'ਪੰਜਾਬੀ': {
    'sidebar': '⚙️ SIH ਪੈਕੇਜਿੰਗ ਇਨਪੁੱਟ',
    'language': '🌐 ਭਾਸ਼ਾ',
    'farmer': 'ਕਿਸਾਨ',
    'seller': 'ਵਿਕਰੇਤਾ',
    'engine': 'AI ਸਿਫਾਰਸ਼ ਇੰਜਣ',
    'farmer_intro': 'ਮੰਡੀ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਉਤਪਾਦ ਲਈ ਵਿਹਾਰਕ ਪੈਕੇਜਿੰਗ ਸਿਫਾਰਸ਼ ਲਵੋ।',
    'seller_intro': 'ਸਟੋਰੇਜ, ਆਵਾਜਾਈ ਅਤੇ ਉਤਪਾਦ ਦੀਆਂ ਸਥਿਤੀਆਂ ਦੇ ਆਧਾਰ ’ਤੇ ਪੈਕੇਜਿੰਗ ਲੋੜਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।',
    'engine_intro': 'ਭੋਜਨ ਗੁਣਾਂ ਅਤੇ ਵਾਤਾਵਰਣੀ ਹਾਲਾਤਾਂ ਨੂੰ ਪੈਕੇਜਿੰਗ ਗਿਆਨ ਅਧਾਰ ਨਾਲ ਮਿਲਾਉਂਦਾ ਹੈ।',
    'generate': '🔍 AI ਸਿਫਾਰਸ਼ ਬਣਾਓ',
    'result': '📦 ਬੁੱਧੀਮਾਨ ਪੈਕੇਜਿੰਗ ਸਿਫਾਰਸ਼',
    'result_desc': 'ਚੁਣੇ ਗਏ ਭੋਜਨ ਅਤੇ ਵਾਤਾਵਰਣੀ ਮਾਪਦੰਡਾਂ ਦੇ ਆਧਾਰ ’ਤੇ ਸਿਫਾਰਸ਼ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ।',
    'analyzed': '🔬 ਵਿਸ਼ਲੇਸ਼ਿਤ ਭੋਜਨ ਅਤੇ ਵਾਤਾਵਰਣ ਗੁਣ',
    'specs': '📋 SIH ਪੈਕੇਜਿੰਗ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ',
    'insights': '💡 ਵਿਹਾਰਕ ਪੈਕੇਜਿੰਗ ਜਾਣਕਾਰੀ',
    'match': '📊 ਸਿਫਾਰਸ਼ ਮਿਲਾਪ',
    'benefits': '👨\u200d🌾 ਕਿਸਾਨ ਅਤੇ 🏪 ਵਿਕਰੇਤਾ ਲਾਭ',
    'flow': '🧠 ਸਮਝਾਉਣਯੋਗ AI ਫੈਸਲਾ ਪ੍ਰਕਿਰਿਆ',
    'sustain': '🌱 ਟਿਕਾਊਪਣ ਅਤੇ ਭੋਜਨ ਬਰਬਾਦੀ ਪ੍ਰਭਾਵ',
    'what': 'ਇਹ ਅਪਗ੍ਰੇਡ ਕੀਤਾ ਪ੍ਰੋਟੋਟਾਈਪ ਕੀ ਦਿਖਾਉਂਦਾ ਹੈ',
    'enter': '👉 ਸਾਈਡਬਾਰ ਵਿੱਚ SIH ਪੈਕੇਜਿੰਗ ਪੈਰਾਮੀਟਰ ਭਰੋ ਅਤੇ **AI ਸਿਫਾਰਸ਼ ਬਣਾਓ** ਤੇ ਕਲਿੱਕ ਕਰੋ।',
    'note': 'ਪ੍ਰੋਟੋਟਾਈਪ ਨੋਟ: ਇਹ ਨਿਯਮ-ਅਧਾਰਿਤ ਫੈਸਲਾ ਸਹਾਇਤਾ ਡੈਮੋ ਹੈ। ਵਪਾਰਕ ਵਰਤੋਂ ਤੋਂ ਪਹਿਲਾਂ OTR/WVTR, MAP ਗੈਸ ਰਚਨਾ, ਸ਼ੈਲਫ ਲਾਈਫ ਅਤੇ ਸਮੱਗਰੀ ਅਨੁਕੂਲਤਾ ਨੂੰ ਲੈਬ ਡੇਟਾ ਅਤੇ ਮਾਹਿਰਾਂ ਨਾਲ ਜਾਂਚਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।',
    'cost_note': '*ਲਾਗਤ ਸਿਰਫ਼ ਪ੍ਰੋਟੋਟਾਈਪ ਅਨੁਮਾਨ ਹੈ ਅਤੇ ਉਤਪਾਦ, ਪੈਕੇਜਿੰਗ ਕਿਸਮ, ਆਵਾਜਾਈ ਦੂਰੀ ਅਤੇ ਸੁਰੱਖਿਆ ਤਰਜੀਹ ਅਨੁਸਾਰ ਬਦਲਦੀ ਹੈ।',
    'storage': '🌡️ ਸਟੋਰੇਜ ਕਿਸਮ',
    'temperature': '🌡️ ਸਟੋਰੇਜ ਤਾਪਮਾਨ (°C)',
    'humidity': '💧 ਸਾਪੇਖ ਨਮੀ (%)',
    'moisture': '💦 ਭੋਜਨ ਨਮੀ',
    'oil': '🫒 ਤੇਲ/ਚਰਬੀ ਸਮੱਗਰੀ',
    'ph': '🧪 pH',
    'respiration': '🫁 ਸਾਹ ਲੈਣ ਦੀ ਦਰ',
    'shelf': '⏳ ਲੋੜੀਂਦੀ ਸ਼ੈਲਫ ਲਾਈਫ (ਦਿਨ)',
    'transport': '🚚 ਆਵਾਜਾਈ',
    'priority': '🎯 ਮੁੱਖ ਤਰਜੀਹ',
    'commodity': '🥬 ਫਸਲ / ਭੋਜਨ ਪਦਾਰਥ',
    'material': 'ਸਿਫਾਰਸ਼ੀ ਸਮੱਗਰੀ',
    'structure': 'ਪੈਕੇਜਿੰਗ ਬਣਤਰ',
    'otr': 'ਆਕਸੀਜਨ ਟ੍ਰਾਂਸਮਿਸ਼ਨ ਲੋੜ (OTR)',
    'wvtr': 'ਪਾਣੀ ਭਾਫ਼ ਟ੍ਰਾਂਸਮਿਸ਼ਨ ਲੋੜ (WVTR)',
    'thickness': 'ਫਿਲਮ/ਬੋਰਡ ਮੋਟਾਈ',
    'sealability': 'ਸੀਲਿੰਗ ਸਮਰੱਥਾ',
    'gas': 'ਗੈਸ ਪਾਰਗਮਤਾ',
    'strength': 'ਮਕੈਨੀਕਲ ਮਜ਼ਬੂਤੀ',
    'map': 'MAP ਯੋਗਤਾ',
    'ventilation': 'ਹਵਾਦਾਰੀ ਲੋੜ',
    'cost': 'ਅਨੁਮਾਨਿਤ ਲਾਗਤ',
    'capacity': 'ਸਮਰੱਥਾ',
    'sustainability': 'ਟਿਕਾਊਪਣ',
    'score': 'ਸਿਫਾਰਸ਼ ਮਿਲਾਪ',
    'vent_need': 'ਹਵਾਦਾਰੀ ਲੋੜ',
    'damage': 'ਨੁਕਸਾਨ ਸੰਵੇਦਨਸ਼ੀਲਤਾ',
    'transport_tag': 'ਆਵਾਜਾਈ',
    'shelf_tag': 'ਸ਼ੈਲਫ ਲਾਈਫ',
    'priority_tag': 'ਤਰਜੀਹ',
    'storage_tag': 'ਸਟੋਰੇਜ',
},
}
language = "English"
def tr(key):
    return LANG[language].get(key, LANG["English"].get(key, key))

# ---------------- PACKAGING KNOWLEDGE BASE ----------------
# Prototype knowledge base. Values are illustrative and should be validated
# with packaging/food-science references before real-world deployment.
packaging_data = {
    "Tomato": {
        "icon":"🍅", "moisture":"High", "oil":"Low", "ph":"4.0–4.5", "respiration":"High",
        "shelf":"3–7 days", "package":"Ventilated Corrugated Box + Food-grade Liner",
        "material":"Food-grade corrugated fibreboard with breathable/food-grade liner",
        "box_type":"Ventilated produce box", "otr":"High", "wvtr":"Moderate",
        "thickness":"3–5 mm board", "seal":"Standard food-grade closure", "gas":"High airflow / breathable",
        "strength":"High", "map":"Limited / condition-dependent", "ventilation":"High", "protection":"High",
        "base_cost":"₹8–₹15 per box*", "capacity":"5–10 kg", "sustain":"High recyclability",
        "farmer":"Helps reduce bruising and physical damage while allowing airflow during transport.",
        "seller":"Supports organized handling and temporary storage while reducing physical damage.",
        "reason":"Tomatoes have high moisture and respiration needs and are sensitive to physical damage. CropSynq therefore balances ventilation with mechanical protection."
    },
    "Potato": {
        "icon":"🥔", "moisture":"Moderate", "oil":"Low", "ph":"5.4–6.5", "respiration":"Moderate",
        "shelf":"1–4 weeks", "package":"Breathable Jute/Corrugated Produce Bag",
        "material":"Breathable jute or food-grade corrugated fibreboard",
        "box_type":"Ventilated produce bag/box", "otr":"High", "wvtr":"Moderate",
        "thickness":"3–5 mm board / suitable jute grade", "seal":"Ventilated closure", "gas":"High airflow",
        "strength":"Medium–High", "map":"Generally not the primary option", "ventilation":"High", "protection":"Medium",
        "base_cost":"₹6–₹14 per pack*", "capacity":"10–20 kg", "sustain":"High recyclability / reusable options",
        "farmer":"Allows air movement and helps reduce moisture accumulation during transportation.",
        "seller":"Supports breathable storage and practical handling of potato produce.",
        "reason":"Potatoes benefit from airflow and moisture management. CropSynq gives priority to breathable packaging."
    },
    "Apple": {
        "icon":"🍎", "moisture":"High", "oil":"Low", "ph":"3.2–4.0", "respiration":"Moderate",
        "shelf":"1–4 weeks", "package":"Partitioned Ventilated Corrugated Fruit Box",
        "material":"Food-grade corrugated fibreboard with partitions/cushioning",
        "box_type":"Partitioned ventilated fruit box", "otr":"Moderate–High", "wvtr":"Moderate",
        "thickness":"3–5 mm board", "seal":"Standard food-grade closure", "gas":"Controlled ventilation",
        "strength":"High", "map":"Possible for controlled cold-chain applications", "ventilation":"High", "protection":"High",
        "base_cost":"₹10–₹20 per box*", "capacity":"5–10 kg", "sustain":"High recyclability",
        "farmer":"Helps protect apples from impact and compression during transportation.",
        "seller":"Improves presentation and reduces physical damage during handling.",
        "reason":"Apples can be damaged by impact and compression. CropSynq therefore considers both ventilation and physical protection."
    },
    "Banana": {
        "icon":"🍌", "moisture":"High", "oil":"Low", "ph":"4.5–5.2", "respiration":"High",
        "shelf":"3–10 days", "package":"Ventilated Corrugated Banana Box",
        "material":"Food-grade corrugated fibreboard",
        "box_type":"Ventilated banana transport box", "otr":"High", "wvtr":"Moderate",
        "thickness":"3–5 mm board", "seal":"Ventilated closure", "gas":"High airflow",
        "strength":"Medium–High", "map":"Condition-dependent", "ventilation":"High", "protection":"Medium",
        "base_cost":"₹8–₹15 per box*", "capacity":"5–10 kg", "sustain":"High recyclability",
        "farmer":"Supports safer transportation while allowing airflow around the produce.",
        "seller":"Helps maintain product quality during handling and market transportation.",
        "reason":"Bananas are sensitive to handling damage and have high respiration. CropSynq balances ventilation and protection."
    },
    "Carrot": {
        "icon":"🥕", "moisture":"High", "oil":"Low", "ph":"5.9–6.4", "respiration":"Moderate",
        "shelf":"1–3 weeks", "package":"Ventilated Produce Crate/Box",
        "material":"Food-grade reusable plastic or corrugated produce container",
        "box_type":"Ventilated produce crate", "otr":"High", "wvtr":"Moderate–High",
        "thickness":"Suitable crate wall / 3–5 mm board", "seal":"Ventilated closure", "gas":"High airflow",
        "strength":"Medium–High", "map":"Condition-dependent", "ventilation":"High", "protection":"Medium",
        "base_cost":"₹8–₹18 per pack*", "capacity":"5–10 kg", "sustain":"Reusable / recyclable options",
        "farmer":"Provides airflow and practical protection during transportation.",
        "seller":"Supports organized handling and reduces unnecessary compression.",
        "reason":"Carrots need airflow and protection from excessive handling pressure. CropSynq recommends ventilated packaging."
    }
}


def estimated_cost(data, commodity, transport, priority):
    """Return a simple illustrative cost range adjusted by packaging/use conditions."""
    base_ranges = {
        "Tomato": (8, 15),
        "Potato": (6, 14),
        "Apple": (10, 20),
        "Banana": (8, 15),
        "Carrot": (8, 18),
    }
    low, high = base_ranges.get(commodity, (8, 15))

    # Long-distance handling generally needs stronger packaging.
    if transport == "Long Distance":
        low += 2
        high += 5

    # A stronger/protective option can add a small packaging cost.
    if priority == "Reduce Damage" and data["protection"] == "High":
        low += 1
        high += 3

    # Keep the result as an illustrative range, not a supplier quotation.
    return f"₹{low}–₹{high} per pack*"


def recommendation_score(data, storage, transport, priority, shelf_days):
    score = 75
    if priority == "Increase Ventilation" and data["ventilation"] == "High": score += 7
    if priority == "Reduce Damage" and data["protection"] == "High": score += 7
    if priority == "Reduce Cost": score += 3
    if transport == "Long Distance": score -= 3 if data["strength"] == "Medium" else 0
    if storage == "Chilled": score += 2
    if storage == "Frozen": score -= 15
    if shelf_days > 14 and data["respiration"] == "High": score -= 4
    return max(60, min(score, 95))

# ---------------- LANGUAGE ----------------
language = st.sidebar.selectbox(tr("language"), list(LANG.keys()))


def spec_label(title):
    mapping = {
        'Recommended Material': "material",
        'Packaging Structure': "structure",
        'Oxygen Transmission Requirement (OTR)': "otr",
        'Water Vapor Transmission Requirement (WVTR)': "wvtr",
        'Film/Board Thickness': "thickness",
        'Sealability': "sealability",
        'Gas Permeability': "gas",
        'Mechanical Strength': "strength",
        'MAP Suitability': "map",
        'Ventilation Requirement': "ventilation",
    }
    return tr(mapping.get(title, title))

# ---------------- HERO ----------------
st.markdown(f"""
<div class="hero">
<h1>🌱 CropSynq</h1>
<p>AI-Based Intelligent Food Packaging Material Recommendation System</p>
<p>{tr("farmer_intro")} | {tr("seller_intro")}</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.title(tr("sidebar"))
commodity = st.sidebar.selectbox(tr("commodity"), list(packaging_data.keys()))
storage = st.sidebar.selectbox(tr("storage"), ["Ambient", "Chilled", "Frozen"])
temperature = st.sidebar.number_input(tr("temperature"), value=25.0, step=1.0)
rh = st.sidebar.slider(tr("humidity"), 30, 100, 70)
moisture_input = st.sidebar.selectbox(tr("moisture"), ["Low", "Moderate", "High"])
oil = st.sidebar.selectbox(tr("oil"), ["Low", "Moderate", "High"])
ph = st.sidebar.number_input(tr("ph"), min_value=1.0, max_value=14.0, value=4.5, step=0.1)
respiration = st.sidebar.selectbox(tr("respiration"), ["Low", "Moderate", "High"])
shelf_days = st.sidebar.number_input(tr("shelf"), min_value=1, max_value=365, value=5)
transport = st.sidebar.selectbox(tr("transport"), ["Local Market", "Wholesale Market", "Long Distance"])
priority = st.sidebar.selectbox(tr("priority"), ["Reduce Damage", "Increase Ventilation", "Reduce Cost", "Increase Shelf Life", "Sustainability"])

st.sidebar.markdown("---")
generate = st.sidebar.button(tr("generate"), use_container_width=True, type="primary")

# ---------------- INTRO ----------------

a,b,c = st.columns(3)
with a:
    st.markdown('<div class="card"><h3>👨‍🌾 {tr("farmer")}</h3><p>{tr("farmer_intro")}</p></div>', unsafe_allow_html=True)
with b:
    st.markdown('<div class="card"><h3>🏪 {tr("seller")}</h3><p>{tr("seller_intro")}</p></div>', unsafe_allow_html=True)
with c:
    st.markdown('<div class="card"><h3>🤖 {tr("engine")}</h3><p>{tr("engine_intro")}</p></div>', unsafe_allow_html=True)

if generate:
    data = packaging_data[commodity]
    score = recommendation_score(data, storage, transport, priority, shelf_days)

    st.markdown('<div class="result"><h2>{tr("result")}</h2><p>{tr("result_desc")}</p></div>', unsafe_allow_html=True)
    st.markdown(f"## {data['icon']} {commodity}")
    st.markdown(f"### 📦 {data['package']}")
    st.write(data["reason"])

    st.markdown(f"<span class='tag'>{tr("storage_tag")}: {storage}</span><span class='tag'>{tr("transport_tag")}: {transport}</span><span class='tag'>{tr("shelf_tag")}: {shelf_days} days</span><span class='tag'>{tr("priority_tag")}: {priority}</span>", unsafe_allow_html=True)

    st.subheader(tr("analyzed"))
    p1,p2,p3,p4 = st.columns(4)
    p1.metric(tr("moisture"), moisture_input)
    p2.metric(tr("oil"), oil)
    p3.metric("pH", f"{ph:.1f}")
    p4.metric("Respiration", respiration)
    p5,p6,p7,p8 = st.columns(4)
    p5.metric(tr("temperature"), f"{temperature:.1f} °C")
    p6.metric(tr("humidity"), f"{rh}%")
    p7.metric(tr("shelf"), f"{shelf_days} days")
    p8.metric(tr("transport"), transport)

    st.subheader(tr("specs"))
    s1,s2 = st.columns(2)
    with s1:
        for title, value in [
            ("Recommended Material", data["material"]),
            ("Packaging Structure", data["box_type"]),
            ("Oxygen Transmission Requirement (OTR)", data["otr"]),
            ("Water Vapor Transmission Requirement (WVTR)", data["wvtr"]),
            ("Film/Board Thickness", data["thickness"])
        ]:
            st.markdown(f"<div class='spec'><b>{spec_label(title)}</b><br>{value}</div>", unsafe_allow_html=True)
    with s2:
        for title, value in [
            ("Sealability", data["seal"]),
            ("Gas Permeability", data["gas"]),
            ("Mechanical Strength", data["strength"]),
            ("MAP Suitability", data["map"]),
            ("Ventilation Requirement", data["ventilation"])
        ]:
            st.markdown(f"<div class='spec'><b>{spec_label(title)}</b><br>{value}</div>", unsafe_allow_html=True)

    st.subheader(tr("insights"))
    i1,i2,i3,i4 = st.columns(4)
    i1.metric(tr("cost"), estimated_cost(data, commodity, transport, priority))
    i2.metric(tr("capacity"), data["capacity"])
    i3.metric(tr("sustainability"), data["sustain"])
    i4.metric(tr("score"), f"{score}%")
    st.caption(tr("cost_note"))

    st.subheader(tr("match"))
    st.progress(score / 100)
    m1,m2,m3 = st.columns(3)
    m1.metric(tr("vent_need"), data["ventilation"])
    m2.metric(tr("damage"), data["protection"])
    m3.metric(tr("respiration"), data["respiration"])

    st.subheader(tr("benefits"))
    b1,b2 = st.columns(2)
    with b1:
        st.markdown(f"<div class='benefit'><h4>👨‍🌾 {tr("farmer")}</h4>{data['farmer']}</div>", unsafe_allow_html=True)
    with b2:
        st.markdown(f"<div class='benefit'><h4>🏪 {tr("seller")}</h4>{data['seller']}</div>", unsafe_allow_html=True)

    st.subheader(tr("flow"))
    flow = [
        f"1️⃣ Commodity → {commodity}",
        f"2️⃣ Food properties → Moisture {moisture_input} | Oil/Fat {oil} | pH {ph:.1f} | Respiration {respiration}",
        f"3️⃣ Environment → {temperature:.1f}°C | RH {rh}% | {storage}",
        f"4️⃣ Logistics → {transport} | Shelf life {shelf_days} days",
        f"5️⃣ Priority → {priority}",
        f"6️⃣ Packaging engine → OTR + WVTR + thickness + sealability + gas permeability + strength + MAP",
        f"7️⃣ Final output → {data['package']}"
    ]
    for step in flow:
        st.markdown(f"<div class='flow'>{step}</div>", unsafe_allow_html=True)

    st.subheader(tr("sustain"))
    st.write("CropSynq can support lower food losses by matching packaging protection and ventilation needs to the commodity and handling conditions. The sustainability field highlights recyclable or reusable packaging alternatives for further evaluation.")

    st.warning(tr("note"))
else:
    st.info(tr("enter"))
    st.markdown("### " + tr("what"))
    st.write("Commodity properties → Environmental conditions → Transportation → AI/rule-based packaging engine → Material + barrier requirements → Packaging recommendation → Explainable decision")

st.caption("CropSynq • SIH 26236 prototype • Multilingual intelligent food packaging decision-support system")
