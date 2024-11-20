from instructions import SYSTEM_INSTRUCTIONS 
import os
import google.generativeai as genai

your_api_key = "AIzaSyDe1R95lbSGFYd7uNmjmK_Zq2vdZPrDr-I"
genai.configure(api_key=your_api_key)

def configure_model(api_key, generation_config):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="meditaciones cortas utilizando la biblia y los escritos de elena g  white.",
    )
    return model



# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="meditaciones cortas utilizando la biblia y los escritos de elena g  white.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "buscame del amo de Cristo\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Meditaciones cortas sobre el Amo de Cristo:\n\n**Meditación 1: La Humildad del Siervo**\n\n**(Filipenses 2:5-8; El Deseado de Todas las Gentes, p. 430)**\n\n*Piensa:* Cristo, siendo Dios, se humilló a sí mismo, tomando forma de siervo.  No vino para ser servido, sino para servir y dar su vida en rescate por muchos. ¿Qué me dice esto sobre el verdadero liderazgo y el amor abnegado? ¿Cómo puedo reflejar esta humildad en mi vida diaria?  Elena G. de White nos recuerda que \"la verdadera grandeza se mide por la norma moral.\"  ¿Estoy buscando la grandeza según los estándares de Dios o los del mundo?\n\n**Meditación 2: El Yugo Suave**\n\n**(Mateo 11:28-30; El Camino a Cristo, p. 67)**\n\n*Reflexiona:* Jesús nos invita a tomar su yugo, prometiendo descanso para nuestras almas. Su yugo no es una carga pesada, sino una guía amorosa.  ¿Qué cargas estoy llevando que Jesús me invita a dejar a sus pies? ¿Cómo puedo experimentar la ligereza y la paz que promete?  Elena G. de White nos anima a \"echar toda nuestra ansiedad sobre Él, porque Él cuida de nosotros\". ¿Confío en la promesa de Jesús de aliviarme?\n\n**Meditación 3: Aprendiendo del Maestro**\n\n**(Mateo 11:29; Los Hechos de los Apóstoles, p. 28)**\n\n*Considera:* Jesús es manso y humilde de corazón.  ¿Qué significa ser manso? No es debilidad, sino fuerza bajo control.  Es una humildad que reconoce nuestra dependencia de Dios. ¿Cómo puedo aprender la mansedumbre de Cristo en mis interacciones con los demás?  Elena G. de White nos enseña que \"la mansedumbre es el fruto del Espíritu Santo.\" ¿Estoy cultivando el fruto del Espíritu en mi vida?\n\n**Meditación 4: El Amor del Amo**\n\n**(Juan 13:1-17; El Deseado de Todas las Gentes, p. 643)**\n\n*Medita:* Jesús lavó los pies de sus discípulos, demostrando un amor humilde y servicial.  ¿Estoy dispuesta/o a realizar las tareas humildes por amor a los demás? ¿Reconozco a Cristo en aquellos que sirven con amor y humildad? Elena G. de White nos recuerda que \"el servicio más humilde, realizado en el nombre de Cristo, ennoblece al que lo realiza.\"  ¿Cómo puedo servir a otros con el mismo amor y humildad de Jesús?\n\n\n**Recuerda:** Estas son solo sugerencias. Dedica tiempo a la oración y a la reflexión personal para que el Espíritu Santo te guíe en tu meditación.  Puedes leer los pasajes bíblicos y los escritos de Elena G. de White citados para profundizar en tu comprensión.\n",
      ],
    },
  ]
)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    try:
        response = chat_session.send_message(user_input)
        print("Model:", response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)

