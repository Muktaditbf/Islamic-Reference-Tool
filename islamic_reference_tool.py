import re
import sys

class IslamicKnowledgeBase:
    def __init__(self):
        """
        Initializes the knowledge base with a dictionary of topics mapping to 
        Quranic verses and Hadith references.
        
        NOTE: In a production environment, this data should come from a verified 
        external API or database (like Quran.com API or Sunnah.com).
        This is a small, manually curated dataset for demonstration.
        """
        self.database = {
            "pork": {
                "topic": "Pork / Swine",
                "status": "Haram (Forbidden)",
                "source": "Quran 2:173",
                "text": "He has only forbidden to you dead animals, blood, the flesh of swine, and that which has been dedicated to other than Allah."
            },
            "swine": "pork",  # Alias
            "pig": "pork",    # Alias
            
            "alcohol": {
                "topic": "Alcohol / Intoxicants (Khamr)",
                "status": "Haram (Forbidden)",
                "source": "Quran 5:90",
                "text": "O you who have believed, indeed, intoxicants, gambling, [sacrificing on] stone alters, and divining arrows are but defilement from the work of Satan, so avoid it that you may be successful."
            },
            "wine": "alcohol",
            "beer": "alcohol",
            "liquor": "alcohol",
            "drinking": "alcohol",

            "gambling": {
                "topic": "Gambling (Maisir)",
                "status": "Haram (Forbidden)",
                "source": "Quran 5:90",
                "text": "Indeed, intoxicants, gambling, [sacrificing on] stone alters... are but defilement from the work of Satan, so avoid it."
            },
            
            "interest": {
                "topic": "Interest / Usury (Riba)",
                "status": "Haram (Forbidden)",
                "source": "Quran 2:275",
                "text": "Those who consume interest cannot stand [on the Day of Resurrection] except as one stands who is being beaten by Satan into insanity... Allah has permitted trade and has forbidden interest."
            },
            "riba": "interest",
            "usury": "interest",
            "loan": "interest",

            "adultery": {
                "topic": "Adultery / Fornication (Zina)",
                "status": "Haram (Forbidden)",
                "source": "Quran 17:32",
                "text": "And do not approach unlawful sexual intercourse. Indeed, it is ever an immorality and is evil as a way."
            },
            "zina": "adultery",
            "sex": "adultery",

            "theft": {
                "topic": "Theft / Stealing",
                "status": "Haram (Forbidden)",
                "source": "Quran 5:38",
                "text": "[As for] the thief, the male and the female, amputate their hands in recompense for what they committed as a deterrent [punishment] from Allah."
            },
            "stealing": "theft",

            "backbiting": {
                "topic": "Backbiting (Gheebah)",
                "status": "Haram (Forbidden)",
                "source": "Quran 49:12",
                "text": "O you who have believed... do not spy or backbite each other. Would one of you like to eat the flesh of his brother when dead? You would detest it."
            },
            "gossip": "backbiting",

            "seafood": {
                "topic": "Seafood / Water Game",
                "status": "Halal (Permissible)",
                "source": "Quran 5:96",
                "text": "Lawful to you is game from the sea and its food as provision for you and the travelers..."
            },
            "fish": "seafood",
            "crab": "seafood",
            "shrimp": "seafood",

            "honey": {
                "topic": "Honey",
                "status": "Halal (Permissible/Beneficial)",
                "source": "Quran 16:69",
                "text": "There emerges from their bellies a drink, varying in colors, in which there is healing for people."
            }
        }

    def search(self, query):
        """
        Scans the query for keywords present in the database.
        Returns a list of result objects.
        """
        query = query.lower()
        # Remove punctuation
        query = re.sub(r'[^\w\s]', '', query)
        words = query.split()
        
        results = []
        found_keys = set()

        for word in words:
            if word in self.database:
                key = word
                # Handle Aliases (e.g., if user types "pig", switch to "pork")
                data_entry = self.database[key]
                if isinstance(data_entry, str):
                    key = data_entry
                    data_entry = self.database[key]
                
                if key not in found_keys:
                    results.append(data_entry)
                    found_keys.add(key)
        
        return results

def print_disclaimer():
    print("\n" + "="*60)
    print("                  ISLAMIC REFERENCE TOOL")
    print("="*60)
    print("⚠️  IMPORTANT DISCLAIMER:")
    print("1. This tool is for EDUCATIONAL and SEARCH purposes only.")
    print("2. It provides direct text from the Quran/Hadith based on keywords.")
    print("3. It DOES NOT issue Fatwas (religious rulings).")
    print("4. Context is crucial in Islam. If you are unsure about a")
    print("   specific personal situation, please consult a qualified Scholar.")
    print("="*60 + "\n")

def main():
    print_disclaimer()
    tool = IslamicKnowledgeBase()

    while True:
        user_input = input("Enter your question (or 'exit' to quit): ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'q']:
            print("Peace be upon you (As-salamu alaykum). Exiting...")
            break
        
        if not user_input:
            continue

        results = tool.search(user_input)

        if results:
            print(f"\nFound {len(results)} reference(s):\n")
            for item in results:
                print(f"🔹 TOPIC:   {item['topic']}")
                print(f"   STATUS:  {item['status']}")
                print(f"   SOURCE:  {item['source']}")
                print(f"   TEXT:    \"{item['text']}\"")
                print("-" * 40)
        else:
            print("\nℹ️  No direct text match found in the embedded database.")
            print("   This does not mean it is Halal or Haram.")
            print("   Please consult a scholar or check a verified Islamic source.")
            print("   (Try keywords like: alcohol, pork, interest, seafood)\n")

if __name__ == "__main__":
    main()