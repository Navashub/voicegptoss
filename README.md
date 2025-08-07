# voicegptoss

# 🎤 Voice Agent with gpt-oss-120b - Openai open source model 

A lightning-fast voice AI agent powered by OpenAI's new gpt-oss-120b model, running locally with Cerebras AI acceleration and Vapi integration. Experience blazing-fast Time To First Token (TTFT) of **0.3-0.7 seconds** for real-time conversational AI.

## ✨ Features

- **Ultra-Low Latency**: TTFT of 0.3-0.7s using OpenAI's gpt-oss-120b model
- **Local Deployment**: Run your voice agent locally with public tunnel access
- **Cerebras AI Acceleration**: Leverages Cerebras AI's inference infrastructure for optimal performance
- **Vapi Integration**: Seamless voice interface through Vapi's telephony platform
- **Real-time Processing**: True real-time voice conversations with minimal delay

## 🚀 Performance

This implementation achieves exceptional performance metrics:
- **Time To First Token (TTFT)**: 0.3-0.7 seconds
- **Model**: OpenAI GPT-4o Realtime (OSS)
- **Infrastructure**: Cerebras AI + Local deployment
- **Latency**: Optimized for real-time voice interactions

## 🛠️ Tech Stack

- **AI Model**: OpenAI gpt-oss-120b
- **Inference**: Cerebras AI
- **Voice Platform**: Vapi
- **Tunneling**: ngrok
- **Backend**: Python
- **Deployment**: Local with public exposure

## 📋 Prerequisites

- Python 3.8+
- Git
- ngrok account and installation
- Cerebras AI API key
- Vapi account

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone git@github.com:Navashub/voicegptoss.git
cd voicegptoss
```

### 2. Set Up Environment
Create a `.env` file in the project root:
```bash
touch .env
```

Add your Cerebras AI API key to the `.env` file:
```env
CEREBRAS_API_KEY=your_cerebras_api_key_here
```

### 3. Get Cerebras AI API Key
1. Visit [Cerebras AI](https://www.cerebras.ai/)
2. Sign up for an account
3. Navigate to API keys section
4. Generate a new API key
5. Copy the key to your `.env` file

### 4. Set Up ngrok
1. Create an account at [ngrok.com](https://ngrok.com/)
2. Install ngrok on your system:
   ```bash
   # Windows (using chocolatey)
   choco install ngrok
   
   # macOS (using homebrew)
   brew install ngrok/ngrok/ngrok
   
   # Linux
   curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
   echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
   sudo apt update && sudo apt install ngrok
   ```
3. Authenticate ngrok with your token:
   ```bash
   ngrok config add-authtoken YOUR_NGROK_AUTHTOKEN
   ```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the Application
```bash
python main.py
```

The application will:
- Start the local server
- Create an ngrok tunnel
- Display the public URL in the console

### 7. Configure Vapi
1. Copy the public ngrok URL from your console output
2. Go to your Vapi dashboard
3. Add the public URL as your webhook endpoint
4. Configure your voice agent settings

### 8. Test Your Voice Agent
Your voice agent is now live and ready to handle calls through Vapi!

## 🔧 Configuration

### Environment Variables
- `CEREBRAS_API_KEY`: Your Cerebras AI API key for model inference
- `NGROK_AUTHTOKEN`: Your ngrok authentication token (optional, can be set via ngrok config)

### Customization
You can modify the voice agent behavior by editing the configuration in `main.py`:
- Adjust model parameters
- Modify response formatting
- Configure webhook endpoints
- Set custom voice settings

## 📊 Performance Optimization

This setup is optimized for minimal latency:
- **Cerebras AI**: Provides fast inference for the GPT-4o model
- **Local Deployment**: Eliminates additional network hops
- **ngrok Tunneling**: Secure public access without complex networking
- **Optimized Code**: Streamlined request/response handling

## 🐛 Troubleshooting

### Common Issues

**ngrok Authentication Error**
```bash
# Make sure you're using the tunnel authtoken, not API key
ngrok config add-authtoken YOUR_TUNNEL_AUTHTOKEN
```

**Cerebras API Key Issues**
- Verify your API key is correctly added to `.env`
- Check your Cerebras AI account has sufficient credits
- Ensure API key has proper permissions

**Connection Issues**
- Check firewall settings
- Verify ngrok tunnel is active
- Confirm webhook URL in Vapi matches ngrok public URL

## 📈 Monitoring

Monitor your voice agent performance:
- Check console logs for TTFT metrics
- Monitor Cerebras AI usage in their dashboard
- Track call quality in Vapi analytics
- Use ngrok dashboard for tunnel statistics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4o Realtime model
- Cerebras AI for high-performance inference
- Vapi for voice interface platform
- ngrok for secure tunneling solution

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review the logs for error details

---

**⚡ Ready to build the future of voice AI? Get started now!**