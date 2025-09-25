import streamlit as st
import random
import pandas as pd

# ---- Jouw playlist (titels + artiesten) ----
songs = [
    "In the End – Linkin Park",
    "What I’ve Done – Linkin Park",
    "Iridescent – Linkin Park",
    "Somewhere I Belong – Linkin Park",
    "Papercut – Linkin Park",
    "One More Light – Linkin Park",
    "Lost – Linkin Park",
    "My December – Linkin Park",
    "Points of Authority – Linkin Park",
    "Figure.09 – Linkin Park",
    "Leave Out All the Rest – Linkin Park",
    "From the Inside – Linkin Park",
    "Breaking the Habit – Linkin Park",
    "Lying from You – Linkin Park",
    "Valentine’s Day – Linkin Park",
    "Hands Held High – Linkin Park",
    "Castle of Glass – Linkin Park",
    "Numb – Linkin Park",
    "Final Masquerade – Linkin Park",
    "Invisible – Linkin Park",
    "Fighting Myself – Linkin Park",
    "The Catalyst – Linkin Park",
    "No Roads Left – Linkin Park",
    "Guilty All the Same (feat. Rakim) – Linkin Park",
    "In My Remains – Linkin Park",
    "Given Up – Linkin Park",
    "Waiting for the End – Linkin Park",
    "Don’t Stay – Linkin Park",
    "Roads Untraveled – Linkin Park",
    "Burning in the Skies – Linkin Park",
    "Hit the Floor – Linkin Park",
    "Heavy (feat. Kiiara) – Linkin Park",
    "Lost in the Echo – Linkin Park",
    "When They Come for Me – Linkin Park",
    "One Step Closer – Linkin Park",
    "Bleed It Out – Linkin Park",
    "The Little Things Give You Away – Linkin Park",
    "Blackout – Linkin Park",
    "Good Goodbye (feat. Pusha T & Stormzy) – Linkin Park",
    "In Between – Linkin Park",
    "We Made It (feat. Busta Rhymes, Linkin Park) – Busta Rhymes, Linkin Park",
    "Powerless – Linkin Park",
    "QWERTY – Linkin Park",
    "Sorry for Now – Linkin Park",
    "Crawling – Linkin Park",
    "Shadow of the Day – Linkin Park",
    "Friendly Fire – Linkin Park",
    "It’s Goin’ Down (feat. Mike Shinoda & Mr. Hahn) – X-Ecutioners, Mike Shinoda, Mr. Hahn",
    "Wastelands – Linkin Park",
    "Points of Authority / 99 Problems / One Step Closer – JAY-Z, Linkin Park",
    "Until It’s Gone – Linkin Park",
    "Burn It Down – Linkin Park",
    "No More Sorrow – Linkin Park",
    "Step Up – Linkin Park",
    "Resolution – Linkin Park",
    "I’ll Be Gone – Linkin Park",
    "With You – Linkin Park",
    "Forgotten – Linkin Park",
    "Easier to Run – Linkin Park",
    "A Place for My Head – Linkin Park",
    "Sharp Edges – Linkin Park",
    "Pushing Me Away – Linkin Park",
    "By Myself – Linkin Park",
    "Blackbirds – Linkin Park",
    "Rebellion (feat. Daron Malakian) – Linkin Park",
    "Numb / Encore – JAY-Z, Linkin Park",
    "Nobody Can Save Me – Linkin Park",
    "A Line in the Sand – Linkin Park",
    "Battle Symphony – Linkin Park",
    "High Voltage – Linkin Park",
    "Robot Boy – Linkin Park",
    "Skin to Bone – Linkin Park",
    "Runaway – Linkin Park",
    "Halfway Right – Linkin Park",
    "Talking to Myself – Linkin Park",
    "All for Nothing (feat. Page Hamilton) – Linkin Park",
    "Not Alone – Linkin Park",
    "The Messenger – Linkin Park",
    "Lies Greed Misery – Linkin Park",
    "Victimized – Linkin Park",
    "Jigga What / Faint – JAY-Z, Linkin Park",
    "In the End (Demo) – Linkin Park",
    "Wretches and Kings – Linkin Park",
    "Keys to the Kingdom – Linkin Park",
    "Until It Breaks – Linkin Park",
    "Nobody’s Listening – Linkin Park",
    "The Emptiness Machine – Linkin Park",
    "Cut the Bridge – Linkin Park",
    "Heavy Is the Crown – Linkin Park",
    "Over Each Other – Linkin Park",
    "Casualty – Linkin Park",
    "Overflow – Linkin Park",
    "Two Faced – Linkin Park",
    "Stained – Linkin Park",
    "Igyieih – Linkin Park",
    "Good Things Go – Linkin Park",
    "Up from the Bottom – Linkin Park",
    "Unshatter – Linkin Park",
    "Let You Fade – Linkin Park",
    "Cure for the Itch – Linkin Park",
    "Faint – Linkin Park",
    "Session – Linkin Park",
    "In Pieces – Linkin Park",
]

# ---- Init state ----
if "pairs" not in st.session_state:
    pairs = [(a, b) for i, a in enumerate(songs) for b in songs[i+1:]]
    random.shuffle(pairs)
    st.session_state.pairs = pairs
if "wins" not in st.session_state:
    st.session_state.wins = {song: 0 for song in songs}

st.title("🎶 Linkin Park Playlist Battle Ranking")

if st.session_state.pairs:
    a, b = st.session_state.pairs.pop()
    st.write("Kies welke je beter vindt:")
    col1, col2 = st.columns(2)
    if col1.button(a):
        st.session_state.wins[a] += 1
    if col2.button(b):
        st.session_state.wins[b] += 1
else:
    st.success("✅ Alle battles gedaan!")
    ranked = sorted(st.session_state.wins.items(), key=lambda x: x[1], reverse=True)
    st.subheader("Eindranking")

    # Toon ranking
    for i, (song, score) in enumerate(ranked, start=1):
        st.write(f"{i}. {song} ({score} punten)")

    # Maak DataFrame
    df = pd.DataFrame(ranked, columns=["Song", "Score"])

    # Downloadknoppen
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download als CSV",
        data=csv,
        file_name="ranking.csv",
        mime="text/csv",
    )

    excel = df.to_excel("ranking.xlsx", index=False)
    with open("ranking.xlsx", "rb") as f:
        st.download_button(
            label="⬇️ Download als Excel",
            data=f,
            file_name="ranking.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
