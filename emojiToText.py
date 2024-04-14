# emoji to text using demoji in python

import demoji

text="🌟 Explore the vast universe of knowledge with endless possibilities. 🌌📚 Let curiosity be your guiding star as you journey through the realms of discovery. 🚀✨ Embrace the adventure that awaits and let your imagination soar beyond the stars. 🌠🔭"

emojis = demoji.findall(text)

for emoji, description in emojis.items():
    print(f"{emoji}: {description}")