
## How to Use

*Screenshots for each step are shown below to make it easy to follow.*
1. **Enter your prompt** in the **Prompt** box.  
   *Example:* `explain the KV cache in one line`
<img width="949" height="351" alt="11" src="https://github.com/user-attachments/assets/f84a1c1c-97ba-43e2-9a85-824f390c8211" />


3. **Pick the number of tokens** to generate.  
   - More tokens = longer output = more time.  
   - For a quick test, try **10–50 tokens**.
<img width="949" height="351" alt="12" src="https://github.com/user-attachments/assets/b36afcd1-5be7-48fb-9a09-c3783b3b200f" />

4. **Turn on KV Cache** by checking the **“KV Cache”** box.  
   - With KV cache on, responses come back **much faster**.
<img width="949" height="351" alt="13" src="https://github.com/user-attachments/assets/44180af0-d14a-4b84-be4c-ce7026c3b9ed" />

5. **See the model’s response** in the **Generation** box.
<img width="953" height="350" alt="7" src="https://github.com/user-attachments/assets/d69d32fe-c47a-4348-991b-0c92ab3ac69b" />

6. **Check the Performance section** to see:  
   - How long the generation took (in seconds)  
<img width="953" height="350" alt="6" src="https://github.com/user-attachments/assets/f2789397-aeb4-4f30-9e12-dc97028faa9c" />

7. **Compare the difference**:  
   - Run the same prompt **without KV cache** by unchecking the box.  
   - You’ll notice the generation takes much longer.
### Example
The screenshot below shows an example:
- With KV cache: 12 seconds
- Without KV cache: 169 seconds
This is roughly a **92% speedup** with the KV cache enabled for this prompt.
<img width="935" height="350" alt="8" src="https://github.com/user-attachments/assets/2087371b-4599-407e-94a3-7cfd688106a6" />
<img width="938" height="337" alt="9" src="https://github.com/user-attachments/assets/688ee5a9-49bf-4380-adde-12d652dbde50" />


7. Use the Clear button to clear the prompt box and reset the number of tokens back to 10.
<img width="935" height="335" alt="10" src="https://github.com/user-attachments/assets/3acad67b-d31a-4e8a-b680-ff4a81a6b346" />





