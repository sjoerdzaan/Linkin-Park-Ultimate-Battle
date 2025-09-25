import streamlit as st
import random
import pandas as pd
import math
from io import BytesIO

# ---- Playlist (103 nummers) ----
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

K = 32  # Elo K-factor

# ---- Init state ----
if "ratings" not in st.session_state:
    st.session_state.ratings = {song: 1000 for song in songs}
if "last_battle" not in st.session_state:
    st.session_state.last_battle = random.sample(songs, 2)

def elo_update(winner, loser):
    Ra = st.session_state.ratings[winner]
    Rb = st.session_state.ratings[loser]
    Ea = 1 / (1 + math.pow(10, (Rb - Ra) / 400))
    Eb = 1 / (1 + math.pow(10, (Ra - Rb) / 400))
    st.session_state.ratings[winner] = Ra + K * (1 - Ea)
    st.session_state.ratings[loser] = Rb + K * (0 - Eb)

st.title("🎶 Linkin Park Playlist Battle (Elo Ranking)")

# ---- Battle ----
a, b = st.session_state.last_battle
st.subheader("Kies welke je beter vindt:")
col1, col2 = st.columns(2)

if col1.button(a):
    elo_update(a, b)
    st.session_state.last_battle = random.sample(songs, 2)
    st.rerun()

if col2.button(b):
    elo_update(b, a)
    st.session_state.last_battle = random.sample(songs, 2)
    st.rerun()

# ---- Ranking ----
st.subheader("📊 Huidige ranking")
ranked = sorted(st.session_state.ratings.items(), key=lambda x: x[1], reverse=True)
df = pd.DataFrame(ranked, columns=["Song", "Elo Rating"])
st.dataframe(df, use_container_width=True)

# ---- Download CSV ----
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇️ Download als CSV",
    data=csv,
    file_name="ranking.csv",
    mime="text/csv",
)

# ---- Download Excel ----
output = BytesIO()
with pd.ExcelWriter(output, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Ranking")
excel_data = output.getvalue()

st.download_button(
    "⬇️ Download als Excel",
    data=excel_data,
    file_name="ranking.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)
