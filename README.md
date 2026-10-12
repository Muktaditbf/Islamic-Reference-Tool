# 📖 Islamic Reference Tool

A command-line Python tool that finds Quranic evidence (*dalil*) for common topics. Type a question in plain English, such as *"Is pork allowed?"* or *"what about interest on a loan"*, and it shows the matching verse, its reference and the general ruling.

> ⚠️ **For education only.** This tool shows source texts. It does **not** issue fatwas (religious rulings). Context matters, so please consult a qualified scholar about personal situations.

## Example

```
Enter your question (or 'exit' to quit): is drinking beer allowed?

Found 1 reference(s):

🔹 TOPIC:   Alcohol / Intoxicants (Khamr)
   STATUS:  Haram (Forbidden)
   SOURCE:  Quran 5:90
   TEXT:    "O you who have believed, indeed, intoxicants, gambling, ..."
```

## How it works

1. Your question is lower-cased and cleaned of punctuation.
2. Each word is looked up in a small, hand-curated knowledge base.
3. **Synonyms** point to the same entry. For example, *pig* and *swine* → pork; *beer*, *wine* and *liquor* → alcohol; *riba* and *usury* → interest.
4. Every matching topic is shown once, with its source.
5. If nothing matches, it says so clearly instead of guessing.

**Topics covered:** pork, alcohol, gambling, interest (riba), adultery (zina), theft, backbiting, seafood and honey.

## Run it

Needs Python 3 and no extra packages.

```bash
python islamic_reference_tool.py
```

Type `exit` to quit.

## Files

| File | Contents |
|---|---|
| `islamic_reference_tool.py` | The search tool and its built-in knowledge base |
| `quran.txt`, `hadith.txt` | Additional verses and hadith in JSON format, for future use |

## Roadmap

- Load `quran.txt` and `hadith.txt` so hadith appear in results too
- Pull verified text from the Quran.com or Sunnah.com APIs instead of a hard-coded list
- Add Bangla and Arabic text
