import streamlit as st
from gtts import gTTS
import base64
import os

# Set page config
st.set_page_config(
    page_title="Hanuman Chalisa",
    page_icon="🕉️",
    layout="wide"
)

# CSS styling
st.markdown("""
<style>
    .title {
        font-size: 2.5em;
        color: #FF5733;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #FF8C00;
        text-align: center;
        margin-bottom: 30px;
    }
    .verse {
        font-size: 1.2em;
        margin-bottom: 15px;
    }
    .hindi {
        font-size: 1.3em;
        font-weight: bold;
        color: #FF5733;
    }
    .english {
        font-style: italic;
        color: #555;
    }
    .audio-container {
        display: flex;
        justify-content: center;
        margin: 30px 0;
    }
</style>
""", unsafe_allow_html=True)

# Audio generation function
def text_to_speech(text, lang='hi'):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_file = "hanuman_chalisa.mp3"
    tts.save(audio_file)
    return audio_file

# Function to create audio player
def audio_player(audio_file):
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    audio_tag = f'''
    <audio controls autoplay style="width: 100%;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    '''
    st.markdown(audio_tag, unsafe_allow_html=True)

# Hanuman Chalisa data
chalisa_data = {
    "doha_start": {
        "hindi": """श्रीगुरु चरन सरोज रज, निज मनु मुकुरु सुधारि।
बरनऊं रघुबर बिमल जसु, जो दायकु फल चारि॥

बुद्धिहीन तनु जानिके, सुमिरौं पवन-कुमार।
बल बुद्धि बिद्या देहु मोहिं, हरहु कलेस बिकार॥""",
        "english": """Shri Guru Charan Saroj Raj, Nij Man Mukur Sudhari
Baranau Raghubar Bimal Jasu, Jo Dayaku Phal Chari

Buddhiheen Tanu Janike, Sumiro Pavan-Kumar
Bal Buddhi Vidya Dehu Mohi, Harahu Kalesh Vikar"""
    },
    "chalisa": [
        {"hindi": "जय हनुमान ज्ञान गुन सागर", "english": "Jai Hanuman Gyan Gun Sagar"},
        {"hindi": "जय कपीस तिहुं लोक उजागर", "english": "Jai Kapis Tihun Lok Ujagar"},
        {"hindi": "रामदूत अतुलित बल धामा", "english": "Ramdoot Atulit Bal Dhama"},
        {"hindi": "अंजनि-पुत्र पवनसुत नामा", "english": "Anjani-Putra Pavan Sut Nama"},
        {"hindi": "महाबीर बिक्रम बजरंगी", "english": "Mahabir Bikram Bajrangi"},
        {"hindi": "कुमति निवार सुमति के संगी", "english": "Kumati Nivar Sumati Ke Sangi"},
        {"hindi": "कंचन बरन बिराज सुबेसा", "english": "Kanchan Baran Biraj Subesa"},
        {"hindi": "कानन कुंडल कुंचित केसा", "english": "Kanan Kundal Kunchit Kesa"},
        {"hindi": "हाथ बज्र औ ध्वजा बिराजै", "english": "Hath Bajra Aur Dhwaja Biraje"},
        {"hindi": "कांधे मूंज जनेऊ साजै", "english": "Kandhe Moonj Janeu Saje"},
        {"hindi": "संकर सुवन केसरीनंदन", "english": "Shankar Suvan Kesari Nandan"},
        {"hindi": "तेज प्रताप महा जग बन्दन", "english": "Tej Pratap Maha Jag Bandan"},
        {"hindi": "विद्यावान गुनी अति चातुर", "english": "Vidyavan Guni Ati Chatur"},
        {"hindi": "राम काज करिबे को आतुर", "english": "Ram Kaj Karibe Ko Aatur"},
        {"hindi": "प्रभु चरित्र सुनिबे को रसिया", "english": "Prabhu Charitra Sunibe Ko Rasiya"},
        {"hindi": "राम लखन सीता मन बसिया", "english": "Ram Lakhan Sita Man Basiya"},
        {"hindi": "सूक्ष्म रूप धरि सियहिं दिखावा", "english": "Sukshma Rup Dhari Siyahi Dikhawa"},
        {"hindi": "विकट रूप धरि लंक जरावा", "english": "Vikat Rup Dhari Lank Jarawa"},
        {"hindi": "भीम रूप धरि असुर संहारे", "english": "Bhim Rup Dhari Asur Sanhare"},
        {"hindi": "रामचंद्र के काज संवारे", "english": "Ramchandra Ke Kaj Sanware"},
        {"hindi": "लाय सजीवन लखन जियाये", "english": "Laye Sanjivan Lakhan Jiyaye"},
        {"hindi": "श्रीरघुबीर हरषि उर लाये", "english": "Shri Raghubir Harashi Ur Laye"},
        {"hindi": "रघुपति कीन्ही बहुत बड़ाई", "english": "Raghupati Kinhi Bahut Badai"},
        {"hindi": "तुम मम प्रिय भरतहि सम भाई", "english": "Tum Mam Priya Bharat-Hi Sam Bhai"},
        {"hindi": "सहस बदन तुम्हरो जस गावैं", "english": "Sahas Badan Tumharo Jas Gaavai"},
        {"hindi": "अस कहि श्रीपति कंठ लगावैं", "english": "Asa Kahi Shripati Kanth Lagavai"},
        {"hindi": "सनकादिक ब्रह्मादि मुनीसा", "english": "Sanakadik Brahmadi Munisa"},
        {"hindi": "नारद सारद सहित अहीसा", "english": "Narad Sarad Sahit Aheesa"},
        {"hindi": "जम कुबेर दिगपाल जहां ते", "english": "Jam Kuber Digpal Jahan Te"},
        {"hindi": "कबि कोबिद कहि सके कहां ते", "english": "Kabi Kovid Kahi Sake Kahan Te"},
        {"hindi": "तुम उपकार सुग्रीवहिं कीन्हा", "english": "Tum Upkar Sugrivahi Kinha"},
        {"hindi": "राम मिलाय राज पद दीन्हा", "english": "Ram Milaye Rajpad Dinha"},
        {"hindi": "तुम्हरो मंत्र बिभीषण माना", "english": "Tumharo Mantra Vibhishan Mana"},
        {"hindi": "लंकेस्वर भए सब जग जाना", "english": "Lankeshwar Bhaye Sab Jag Jana"},
        {"hindi": "जुग सहस्र जोजन पर भानू", "english": "Jug Sahastra Jojan Par Bhanu"},
        {"hindi": "लील्यो ताहि मधुर फल जानू", "english": "Leelyo Tahi Madhur Phal Janu"},
        {"hindi": "प्रभु मुद्रिका मेलि मुख माहीं", "english": "Prabhu Mudrika Meli Mukh Mahi"},
        {"hindi": "जलधि लांघि गये अचरज नाहीं", "english": "Jaladhi Langhi Gaye Acharaj Nahi"},
        {"hindi": "दुर्गम काज जगत के जेते", "english": "Durgam Kaj Jagat Ke Jete"},
        {"hindi": "सुगम अनुग्रह तुम्हरे तेते", "english": "Sugam Anugraha Tumhare Tete"},
        {"hindi": "राम दुआरे तुम रखवारे", "english": "Ram Duware Tum Rakhavare"},
        {"hindi": "होत न आज्ञा बिनु पैसारे", "english": "Hot Na Agya Binu Paisare"},
        {"hindi": "सब सुख लहै तुम्हारी सरना", "english": "Sab Sukh Lahai Tumhari Sarna"},
        {"hindi": "तुम रक्षक काहू को डर ना", "english": "Tum Rakshak Kahu Ko Darna"},
        {"hindi": "आपन तेज सम्हारो आपै", "english": "Aapan Tej Samharo Aapai"},
        {"hindi": "तीनों लोक हांक तें कांपै", "english": "Teenon Lok Hank Te Kanpai"},
        {"hindi": "भूत पिसाच निकट नहिं आवै", "english": "Bhoot Pishach Nikat Nahi Aavai"},
        {"hindi": "महाबीर जब नाम सुनावै", "english": "Mahabir Jab Naam Sunavai"},
        {"hindi": "नासै रोग हरै सब पीरा", "english": "Nasai Rog Hare Sab Peera"},
        {"hindi": "जपत निरंतर हनुमत बीरा", "english": "Japat Nirantar Hanumat Beera"},
        {"hindi": "संकट तें हनुमान छुड़ावै", "english": "Sankat Te Hanuman Chhudavai"},
        {"hindi": "मन क्रम बचन ध्यान जो लावै", "english": "Man Kram Bachan Dhyan Jo Lavai"},
        {"hindi": "सब पर राम तपस्वी राजा", "english": "Sab Par Ram Tapasvee Raja"},
        {"hindi": "तिन के काज सकल तुम साजा", "english": "Tin Ke Kaj Sakal Tum Saja"},
        {"hindi": "और मनोरथ जो कोई लावै", "english": "Aur Manorath Jo Koi Lavai"},
        {"hindi": "सोई अमित जीवन फल पावै", "english": "Soi Amit Jeevan Phal Pavai"},
        {"hindi": "चारों जुग परताप तुम्हारा", "english": "Charon Jug Partap Tumhara"},
        {"hindi": "है परसिद्ध जगत उजियारा", "english": "Hai Parasiddh Jagat Ujiyara"},
        {"hindi": "साधु-संत के तुम रखवारे", "english": "Sadhu Sant Ke Tum Rakhvare"},
        {"hindi": "असुर निकंदन राम दुलारे", "english": "Asur Nikandan Ram Dulare"},
        {"hindi": "अष्ट सिद्धि नौ निधि के दाता", "english": "Ashta Siddhi Nav Nidhi Ke Data"},
        {"hindi": "अस बर दीन जानकी माता", "english": "As Var Deen Janki Mata"},
        {"hindi": "राम रसायन तुम्हरे पासा", "english": "Ram Rasayan Tumhare Pasa"},
        {"hindi": "सदा रहो रघुपति के दासा", "english": "Sada Raho Raghupati Ke Dasa"},
        {"hindi": "तुम्हरे भजन राम को पावै", "english": "Tumhare Bhajan Ram Ko Pavai"},
        {"hindi": "जनम-जनम के दुख बिसरावै", "english": "Janam-Janam Ke Dukh Bisravai"},
        {"hindi": "अन्तकाल रघुबर पुर जाई", "english": "Antkaal Raghubar Pur Jai"},
        {"hindi": "जहां जन्म हरि-भक्त कहाई", "english": "Jahan Janam Hari-Bhakt Kahai"},
        {"hindi": "और देवता चित्त न धरई", "english": "Aur Devta Chitta Na Dharai"},
        {"hindi": "हनुमत सेई सर्व सुख करई", "english": "Hanumat Sei Sarv Sukh Karai"},
        {"hindi": "संकट कटै मिटै सब पीरा", "english": "Sankat Kate Mite Sab Peera"},
        {"hindi": "जो सुमिरै हनुमत बलबीरा", "english": "Jo Sumirai Hanumat Balbeera"},
        {"hindi": "जै जै जै हनुमान गोसाईं", "english": "Jai Jai Jai Hanuman Gosai"},
        {"hindi": "कृपा करहु गुरुदेव की नाईं", "english": "Kripa Karahu Gurudev Ki Nai"},
        {"hindi": "जो शत बार पाठ कर कोई", "english": "Jo Shat Bar Path Kar Koi"},
        {"hindi": "छूटहि बंदि महा सुख होई", "english": "Chhutahi Bandi Maha Sukh Hoi"},
        {"hindi": "जो यह पढ़ै हनुमान चालीसा", "english": "Jo Yah Padhe Hanuman Chalisa"},
        {"hindi": "होय सिद्धि साखी गौरीसा", "english": "Hoye Siddhi Sakhi Gaurisa"},
        {"hindi": "तुलसीदास सदा हरि चेरा", "english": "Tulsidas Sada Hari Chera"},
        {"hindi": "कीजै नाथ हृदय मंह डेरा", "english": "Kije Nath Hriday Mah Dera"}
    ],
    "doha_end": {
        "hindi": """पवन तनय संकट हरन, मंगल मूरति रूप।
राम लखन सीता सहित, हृदय बसहु सुर भूप॥""",
        "english": """Pavan Tanay Sankat Haran, Mangal Moorati Roop
Ram Lakhan Sita Sahit, Hriday Basahu Sur Bhoop"""
    }
}

# Main app
def main():
    # Header
    st.markdown('<div class="title">श्री हनुमान चालीसा</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Hanuman Chalisa with Audio</div>', unsafe_allow_html=True)
    
    # Audio section
    st.markdown("### Listen to Hanuman Chalisa")
    
    # Generate audio file
    full_text = "\n".join([verse["hindi"] for verse in chalisa_data["chalisa"]])
    audio_file = text_to_speech(full_text, lang='hi')
    
    # Display audio player
    st.markdown('<div class="audio-container">', unsafe_allow_html=True)
    audio_player(audio_file)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Doha at start
    st.markdown("### दोहा (Doha)")
    st.markdown(f'<div class="hindi">{chalisa_data["doha_start"]["hindi"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="english">{chalisa_data["doha_start"]["english"]}</div>', unsafe_allow_html=True)
    
    # Chalisa verses
    st.markdown("### चौपाई (Chaupai)")
    for i, verse in enumerate(chalisa_data["chalisa"], 1):
        st.markdown(f'<div class="verse">{i}. <span class="hindi">{verse["hindi"]}</span><br><span class="english">{verse["english"]}</span></div>', unsafe_allow_html=True)
    
    # Doha at end
    st.markdown("### दोहा (Doha)")
    st.markdown(f'<div class="hindi">{chalisa_data["doha_end"]["hindi"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="english">{chalisa_data["doha_end"]["english"]}</div>', unsafe_allow_html=True)
    
    # Clean up audio file
    if os.path.exists(audio_file):
        os.remove(audio_file)

if __name__ == "__main__":
    main()