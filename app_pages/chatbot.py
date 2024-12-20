import streamlit as st
import ollama

# Title and Introduction
st.title("🤖 :rainbow[Wall-E]")
st.write("A chatbot powered by **Llama3.2**. Ask me anything!")

# Initialize chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    
# Clear Chat History Button
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    
st.sidebar.button('🗑️ Clear Chat History', on_click=clear_chat_history)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input Box
prompt = st.chat_input(placeholder="Type your message here...")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response from the assistant
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Call Ollama to generate a response
                result = ollama.chat(
                    model="llama3.2",
                    messages=[{"role": "user", "content": prompt}]
                )
                response = result["message"]["content"]
                
                # Use a placeholder to stream the response incrementally
                placeholder = st.empty()
                full_response = ""
                for chunk in response:  # Assuming `response` is an iterable generator
                    full_response += chunk
                    placeholder.markdown(full_response)  # Update placeholder dynamically

                # Final response
                placeholder.markdown(full_response)

                # Append assistant's response to the chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})

            except Exception as e:
                # Handle any exceptions and display an error message
                error_message = "An error occurred while processing your request. Please try again."
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Add Download Button in Sidebar
st.sidebar.download_button(
    label="💾 Download Chat History",
    data=str(st.session_state.messages),
    file_name="chat_history.txt",
    mime="text/plain"
)      