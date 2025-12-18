# import streamlit as st
# from huggingface_hub import InferenceClient

# # 1. Page Configuration
# st.set_page_config(page_title="Zalim AI Pro", page_icon="⚡", layout="centered")

# # Custom CSS for "Zalim" Premium Look
# st.markdown("""
#     <style>
#     .stApp { background-color: #050505; color: #e0e0e0; }
#     .stChatMessage { border-radius: 15px; margin-bottom: 10px; border: 1px solid #333; }
#     .stChatInputContainer { padding-bottom: 20px; }
#     section[data-testid="stSidebar"] { background-color: #111; border-right: 1px solid #222; }
#     .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; border: none; }
#     /* Gradient Title */
#     .main-title {
#         font-size: 50px;
#         font-weight: 800;
#         background: -webkit-linear-gradient(#eee, #333);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         text-align: center;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # 2. Sidebar Settings
# with st.sidebar:
#     st.markdown("<h1 style='text-align: center;'>⚡ Settings</h1>", unsafe_allow_html=True)
#     hf_token = st.text_input("Hugging Face Token:", type="password", help="Apna token yahan dalein")
    
#     st.divider()
#     model_id = st.selectbox("Model Select Karein:", [
#         "meta-llama/Meta-Llama-3-8B-Instruct",
#         "mistralai/Mixtral-8x7B-Instruct-v0.1",
#         "google/gemma-1.1-7b-it"
#     ])
    
#     temp = st.slider("Creativity (Temperature):", 0.1, 1.0, 0.7)
#     max_tokens = st.slider("Max Length:", 128, 4096, 1024)
    
#     if st.button("🗑️ Clear Chat History"):
#         st.session_state.messages = []
#         st.rerun()

# st.markdown('<p class="main-title">ZALIM AI PRO</p>', unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color: #888;'>Duniya ka sab se khatarnak open-source chatbot</p>", unsafe_allow_html=True)

# # 3. Initialize Chat History
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display Chat History with Icons
# for message in st.session_state.messages:
#     avatar = "👤" if message["role"] == "user" else "🤖"
#     with st.chat_message(message["role"], avatar=avatar):
#         st.markdown(message["content"])

# # 4. Chat Logic
# if prompt := st.chat_input("Bhai se kya poochna hai?"):
#     if not hf_token:
#         st.warning("⚠️ Oye! Pehle Sidebar mein Token toh dalo!")
#         st.stop()

#     # User Message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user", avatar="👤"):
#         st.markdown(prompt)

#     # Bot Response
#     try:
#         client = InferenceClient(model_id, token=hf_token)
        
#         with st.chat_message("assistant", avatar="🤖"):
#             response_placeholder = st.empty()
#             full_response = ""
            
#             # API Call with Streaming & Error Check
#             stream = client.chat_completion(
#                 st.session_state.messages,
#                 max_tokens=max_tokens,
#                 temperature=temp,
#                 stream=True,
#             )

#             for message in stream:
#                 # Range Index Error Fix: Check if choices exists
#                 if hasattr(message, 'choices') and len(message.choices) > 0:
#                     token = message.choices[0].delta.content
#                     if token is not None:
#                         full_response += token
#                         response_placeholder.markdown(full_response + "▌")
            
#             response_placeholder.markdown(full_response)
#             st.session_state.messages.append({"role": "assistant", "content": full_response})
            
#     except Exception as e:
#         st.error(f"Zalim Error: {str(e)}")
import streamlit as st
from huggingface_hub import InferenceClient

# 1. Page Configuration
st.set_page_config(page_title="Zalim AI Lite", page_icon="✨", layout="centered")

# Custom CSS for "Zalim" Light & Clean Look
st.markdown("""
    <style>
    /* Background and Text */
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] { background-color: #f8f9fa; border-right: 1px solid #eee; }
    
    /* Chat Bubbles Styling */
    .stChatMessage { 
        border-radius: 20px; 
        padding: 15px;
        margin-bottom: 15px; 
        border: 1px solid #f0f0f0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
    
    /* Input Box Styling */
    .stChatInputContainer { padding-bottom: 30px; background-color: transparent; }
    
    /* Button Styling */
    .stButton>button { 
        border-radius: 10px; 
        background-color: #f0f2f6; 
        color: #333; 
        border: 1px solid #ddd;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ff4b4b; color: white; border: none; }

    /* Modern Header */
    .main-title {
        font-size: 45px;
        font-weight: 700;
        color: #222;
        text-align: center;
        letter-spacing: -1px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Settings
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #333;'>⚙️ Settings</h2>", unsafe_allow_html=True)
    hf_token = st.text_input("Hugging Face Token:", type="password", placeholder="Paste your token here...")
    
    st.divider()
    model_id = st.selectbox("Intelligence Level:", [
        "meta-llama/Meta-Llama-3-8B-Instruct",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "google/gemma-1.1-7b-it"
    ])
    
    temp = st.slider("Creativity:", 0.1, 1.0, 0.7)
    max_tokens = st.slider("Response Length:", 128, 4096, 1024)
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

st.markdown('<p class="main-title">ZALIM AI <span style="color:#ff4b4b">LITE</span></p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Clean. Fast. Intelligent.</p>", unsafe_allow_html=True)

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    avatar = "https://cdn-icons-png.flaticon.com/512/3177/3177440.png" if message["role"] == "user" else "https://cdn-icons-png.flaticon.com/512/4712/4712035.png"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 4. Chat Logic
if prompt := st.chat_input("Bhai se kuch bhi pucho..."):
    if not hf_token:
        st.info("💡 Bhai, pehle sidebar mein apna API token daal do.")
        st.stop()

    # User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="https://cdn-icons-png.flaticon.com/512/3177/3177440.png"):
        st.markdown(prompt)

    # Bot Response
    try:
        client = InferenceClient(model_id, token=hf_token)
        
        with st.chat_message("assistant", avatar="https://cdn-icons-png.flaticon.com/512/4712/4712035.png"):
            response_placeholder = st.empty()
            full_response = ""
            
            stream = client.chat_completion(
                st.session_state.messages,
                max_tokens=max_tokens,
                temperature=temp,
                stream=True,
            )

            for message in stream:
                # Robust index check
                if hasattr(message, 'choices') and len(message.choices) > 0:
                    token = message.choices[0].delta.content
                    if token is not None:
                        full_response += token
                        response_placeholder.markdown(full_response + " ")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
    except Exception as e:
        st.error(f"Error: {str(e)}")