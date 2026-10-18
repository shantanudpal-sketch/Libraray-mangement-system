
import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8001"

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==================== BLACK & WHITE THEME ====================
st.markdown("""
<style>
:root {
    --espresso: #30231D;
    --coffee: #8B5E3C;
    --caramel: #B77945;
    --cream: #F7F2EA;
    --card: #FFFCF7;
    --line: #E7D9C8;
    --muted: #786455;
}

.stApp {
    background: var(--cream) !important;
    color: var(--espresso) !important;
}
.block-container {
    max-width: 1550px;
    padding: 1.5rem 2rem 3rem;
}

/* Sidebar */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div:first-child {
    background: var(--espresso) !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #FFF8EF !important;
}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color: #D4BFA8 !important;
}
.sidebar-menu-label {
    color: #EAD8C5;
    font-size: .76rem;
    font-weight: 750;
    letter-spacing: 1px;
    padding: 8px 10px 12px;
}
[data-testid="stSidebar"] div.stButton > button {
    min-height: 44px;
    width: 100%;
    padding: 9px 12px;
    margin: 2px 0;
    border-radius: 10px;
    text-align: left;
    font-weight: 600;
    transition: background .18s ease, border-color .18s ease;
}
[data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
    background: transparent !important;
    color: #F7EBDD !important;
    border: 1px solid transparent !important;
}
[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
    background: #49372C !important;
    border-color: #6B4C37 !important;
    color: #FFFFFF !important;
}
[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background: var(--caramel) !important;
    color: #FFFFFF !important;
    border: 1px solid #C68B56 !important;
    box-shadow: 0 3px 10px rgba(0, 0, 0, .12);
}
[data-testid="stSidebar"] hr {
    border-color: #604A3B !important;
}

/* Typography */
h1, h2, h3 {
    color: var(--espresso) !important;
    letter-spacing: -.25px;
}
p, label {
    color: #59483D;
}

/* Top welcome banner */
.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 23px 25px;
    margin-bottom: 26px;
    box-shadow: 0 4px 16px rgba(69, 45, 29, .06);
}
.brand {
    color: var(--espresso) !important;
    font-size: 1.7rem;
    font-weight: 800;
    letter-spacing: -.7px;
    line-height: 1.35;
}
.brand-caption {
    color: var(--muted) !important;
    font-size: .98rem;
    line-height: 1.6;
    margin-top: 7px;
}
.admin-pill {
    background: #F2E3D2 !important;
    color: #704522 !important;
    border: 1px solid #E3C7A7 !important;
    padding: 10px 14px;
    border-radius: 999px;
    font-size: .76rem;
    font-weight: 750;
    white-space: nowrap;
}

/* Metric cards */
.metric-card {
    background: var(--card) !important;
    border: 1px solid var(--line) !important;
    border-top: 3px solid var(--caramel) !important;
    border-radius: 14px;
    padding: 21px;
    min-height: 135px;
    box-shadow: 0 4px 14px rgba(69, 45, 29, .05);
    transition: transform .18s ease, box-shadow .18s ease;
}
.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(69, 45, 29, .09);
}
.metric-label {
    color: var(--muted) !important;
    font-size: .8rem;
    font-weight: 750;
    letter-spacing: .5px;
}
.metric-value {
    color: var(--espresso) !important;
    font-size: 2.2rem;
    font-weight: 800;
    margin-top: 10px;
}
.metric-note {
    color: #8A7767 !important;
    font-size: .8rem;
    margin-top: 7px;
}

/* Buttons */
div.stButton > button,
div.stFormSubmitButton > button {
    border-radius: 9px;
    min-height: 42px;
    font-weight: 650;
    transition: all .18s ease;
}
div.stButton > button[kind="primary"],
div.stFormSubmitButton > button[kind="primary"] {
    background: var(--coffee) !important;
    color: #FFFFFF !important;
    border-color: var(--coffee) !important;
}
div.stButton > button[kind="primary"]:hover,
div.stFormSubmitButton > button[kind="primary"]:hover {
    background: #704522 !important;
    border-color: #704522 !important;
}

/* Forms, inputs, tables and alerts */
div[data-testid="stForm"] {
    background: var(--card);
    border: 1px solid var(--line) !important;
    border-radius: 14px;
    padding: 22px;
}
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid var(--line) !important;
    border-radius: 10px;
    overflow: hidden;
}
[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 16px;
}
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 9px;
}
[data-testid="stAlert"] {
    border-radius: 11px;
}

/* Footer */
.footer {
    text-align: center;
    color: #8A7767 !important;
    font-size: .78rem;
    padding-top: 25px;
    margin-top: 20px;
    border-top: 1px solid var(--line) !important;
}

/* Smaller screens */
@media (max-width: 900px) {
    .block-container { padding: 1rem 1rem 2rem; }
    .topbar { padding: 17px; align-items: flex-start; }
    .brand { font-size: 1.3rem; }
    .brand-caption { font-size: .88rem; }
    .admin-pill { font-size: .65rem; padding: 7px 9px; }
}
</style>

""", unsafe_allow_html=True)


# ==================== HELPERS ====================
def fetch_books():
    response = requests.get(f"{API_URL}/books", timeout=5)
    response.raise_for_status()
    return response.json()


def connection_error():
    st.error(
        "Cannot connect to FastAPI. Ensure the backend is running "
        "at http://127.0.0.1:8001."
    )


def api_error(response, action):
    try:
        detail = response.json().get("detail", response.text)
    except ValueError:
        detail = response.text
    st.error(f"{action} failed: {detail}")


def render_header(title, subtitle, section="LIBRARY MANAGEMENT"):
    st.markdown(
        f'<div class="eyebrow">{section}</div>',
        unsafe_allow_html=True,
    )
    st.title(title)
    st.markdown(
        f'<div class="subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )


def render_metric(label, value, note):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_table(books):
    if not books:
        st.info("No book records available.")
        return

    df = pd.DataFrame(books).rename(columns={
        "id": "Book ID",
        "title": "Book Title",
        "author": "Author",
    })
    st.dataframe(df, hide_index=True, use_container_width=True)


def find_book(books, book_id):
    return next((b for b in books if b["id"] == book_id), None)


def get_author_counts(books):
    counts = {}
    for book in books:
        author = book["author"].strip() or "Unknown"
        counts[author] = counts.get(author, 0) + 1
    return counts


# ==================== SIDEBAR ====================
st.sidebar.markdown("## 📚 Library Management")
st.sidebar.caption("LIBRARY MANAGEMENT SYSTEM")
st.sidebar.divider()

page_icons = {
    "Dashboard": "🏠",
    "View Books": "📚",
    "Add Book": "➕",
    "Update Book": "✏️",
    "Delete Book": "🗑️",
    "Search Books": "🔍",
    "Statistics": "📊",
    "Book Details": "📖",
    "About": "ℹ️",
}

# Button-based navigation: no radio circles
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Dashboard"

st.sidebar.markdown(
    '<div class="sidebar-menu-label">MAIN MENU</div>',
    unsafe_allow_html=True,
)

def select_page(selected_page):
    st.session_state["current_page"] = selected_page

for menu_item, menu_icon in page_icons.items():
    is_active = st.session_state["current_page"] == menu_item
    st.sidebar.button(
        f"{menu_icon}   {menu_item}",
        key=f"nav_{menu_item.lower().replace(' ', '_')}",
        on_click=select_page,
        args=(menu_item,),
        type="primary" if is_active else "secondary",
        use_container_width=True,
    )

page = st.session_state["current_page"]

st.sidebar.divider()
st.sidebar.caption("Version 1.0")
st.sidebar.caption("Streamlit · FastAPI · PostgreSQL")


# ==================== TOP HEADER ====================
# This stays at the top of every page.

st.markdown("""
<div class="topbar">
    <div>
        <div class="brand">Welcome to Library Management System 📚</div>
        <div class="brand-caption">
            Manage your books, explore the catalogue, and track library records in one place.
        </div>
    </div>
    <div class="admin-pill">ADMIN WORKSPACE</div>
</div>
""", unsafe_allow_html=True)



# ==================== 1. DASHBOARD ====================
if page == "Dashboard":
    

    try:
        books = fetch_books()
        counts = get_author_counts(books)

        total = len(books)
        unique_authors = len(counts)
        unique_titles = len({
            b["title"].strip().casefold() for b in books
        })

        c1, c2, c3 = st.columns(3, gap="medium")
        with c1:
            render_metric("TOTAL BOOK RECORDS", total, "All saved records")
        with c2:
            render_metric("UNIQUE AUTHORS", unique_authors, "Distinct authors")
        with c3:
            render_metric("UNIQUE TITLES", unique_titles, "Distinct titles")

        st.write("")
        st.success("Connected to FastAPI and PostgreSQL.")
        
        st.markdown("### Quick Actions")
        action1, action2, action3 = st.columns(3, gap="medium")

        with action1:
            if st.button("➕ Add Book", use_container_width=True):
                st.session_state["current_page"] = "Add Book"
                st.rerun()

        with action2:
            if st.button("🔍 Search Books", use_container_width=True):
                st.session_state["current_page"] = "Search Books"
                st.rerun()

        with action3:
            if st.button("📚 View Books", use_container_width=True):
                st.session_state["current_page"] = "View Books"
                st.rerun()


        chart_col, recent_col = st.columns([1, 1], gap="large")

        with chart_col:
            st.subheader("Author Distribution")
            st.caption("Share of book records by author")

            if counts:
                donut_df = pd.DataFrame(
                    list(counts.items()),
                    columns=["Author", "Book Records"],
                )

                st.vega_lite_chart(
                    donut_df,
                    {
                        "layer": [
                            {
                                "mark": {
                                    "type": "arc",
                                    "innerRadius": 68,
                                    "stroke": "#FFFFFF",
                                    "strokeWidth": 3,
                                },
                                "encoding": {
                                    "theta": {
                                        "field": "Book Records",
                                        "type": "quantitative",
                                    },
                                    "color": {
                                        "field": "Author",
                                        "type": "nominal",
                                        "scale": {
                                            "range": [
                                                "#30231D",
                                                "#8B5E3C",
                                                "#B77945",
                                                "#CDA982",
                                                "#E7D9C8",
                                            ]
                                        },
                                        "legend": {
                                            "title": "Author",
                                            "orient": "bottom",
                                        },
                                    },
                                    "tooltip": [
                                        {"field": "Author", "type": "nominal"},
                                        {
                                            "field": "Book Records",
                                            "type": "quantitative",
                                        },
                                    ],
                                },
                            },
                            {
                                "data": {"values": [{"label": "TOTAL BOOKS", "count": total}]},
                                "mark": {
                                    "type": "text",
                                    "fontSize": 11,
                                    "fontWeight": 600,
                                    "color": "#666666",
                                    "dy": -10,
                                },
                                "encoding": {"text": {"field": "label"}},
                            },
                            {
                                "data": {"values": [{"count": total}]},
                                "mark": {
                                    "type": "text",
                                    "fontSize": 28,
                                    "fontWeight": 800,
                                    "color": "#142D4E",
                                    "dy": 17,
                                },
                                "encoding": {
                                    "text": {"field": "count", "type": "quantitative"}
                                },
                            },
                        ],
                        "resolve": {"scale": {"color": "independent"}},
                        "view": {"stroke": None},
                        "background": "#F7F2EA",
                        "width": "container",
                        "height": 280,
                    },
                    use_container_width=True,
                )
            else:
                st.info("Add a book to display the chart.")

        with recent_col:
            st.subheader("Recently Added")
            st.caption("Latest five records")

            if books:
                recent = sorted(
                    books,
                    key=lambda b: b["id"],
                    reverse=True,
                )[:5]
                render_table(recent)
            else:
                st.info("No recent records.")

        # Quick insight summary based on the current database records.
        if books:
            st.divider()
            st.subheader("Quick Insights")

            author_total = max(counts.values())
            top_authors = [
                name for name, count in counts.items()
                if count == author_total
            ]

            insight_col1, insight_col2 = st.columns(2, gap="medium")

            with insight_col1:
                st.markdown("**Author with most records**")

                if len(top_authors) == 1:
                    st.write(
                        f"{top_authors[0]} · {author_total} book record(s)"
                    )
                else:
                    st.write(
                        f"Tie — {author_total} record(s) each: "
                        f"{', '.join(top_authors)}"
                    )

            with insight_col2:
                st.markdown("**Catalogue Summary**")
                st.write(
                    f"{total} book record(s) · "
                    f"{unique_titles} unique title(s) · "
                    f"{unique_authors} author(s)."
                )

        st.markdown(
            '<div class="footer">Library Management System · Streamlit · FastAPI · PostgreSQL</div>',
            unsafe_allow_html=True,
        )

    except requests.RequestException:
        connection_error()


# ==================== 2. VIEW BOOKS ====================
elif page == "View Books":
    render_header(
        "Book Catalogue",
        "Browse all records stored in the library.",
        "CATALOGUE",
    )
    try:
        books = fetch_books()
        if not books:
            st.info("The catalogue is empty. Add your first book.")
        else:
            st.metric("Total Book Records", len(books))
            render_table(books)
    except requests.RequestException:
        connection_error()


# ==================== 3. ADD BOOK ====================
elif page == "Add Book":
    render_header(
        "Add New Book",
        "Enter the details required to create a book record.",
        "CATALOGUE MANAGEMENT",
    )

    with st.form("add_book_form", clear_on_submit=True):
        title = st.text_input("Book Title *", placeholder="Enter book title")
        author = st.text_input("Author Name *", placeholder="Enter author name")
        st.caption("* Required fields")

        submitted = st.form_submit_button(
            "ADD BOOK",
            type="primary",
            use_container_width=True,
        )

        if submitted:
            if not title.strip() or not author.strip():
                st.warning("Both fields are required.")
            else:
                try:
                    response = requests.post(
                        f"{API_URL}/books",
                        json={
                            "title": title.strip(),
                            "author": author.strip(),
                        },
                        timeout=5,
                    )
                    if response.status_code in (200, 201):
                        st.success("Book added successfully!")
                        st.json(response.json())
                    else:
                        api_error(response, "Adding book")
                except requests.RequestException:
                    connection_error()


# ==================== 4. UPDATE BOOK ====================
elif page == "Update Book":
    render_header(
        "Update Book",
        "Select a record and update its information.",
        "CATALOGUE MANAGEMENT",
    )
    try:
        books = fetch_books()
        if not books:
            st.info("No books available to update.")
        else:
            selected_id = st.selectbox(
                "Select Book ID",
                [b["id"] for b in books],
            )
            selected = find_book(books, selected_id)
            st.info(f"Selected: {selected['title']} — {selected['author']}")

            with st.form("update_book_form"):
                title = st.text_input("Book Title *", value=selected["title"])
                author = st.text_input("Author Name *", value=selected["author"])

                submitted = st.form_submit_button(
                    "SAVE CHANGES",
                    type="primary",
                    use_container_width=True,
                )

                if submitted:
                    if not title.strip() or not author.strip():
                        st.warning("Title and author cannot be empty.")
                    else:
                        response = requests.put(
                            f"{API_URL}/books/{selected_id}",
                            json={
                                "title": title.strip(),
                                "author": author.strip(),
                            },
                            timeout=5,
                        )
                        if response.status_code == 200:
                            st.success("Book updated successfully!")
                            st.json(response.json())
                        else:
                            api_error(response, "Updating book")
    except requests.RequestException:
        connection_error()


# ==================== 5. DELETE BOOK ====================
elif page == "Delete Book":
    render_header(
        "Delete Book",
        "Review the record before permanently deleting it.",
        "CATALOGUE MANAGEMENT",
    )
    try:
        books = fetch_books()
        if not books:
            st.info("No books available to delete.")
        else:
            selected_id = st.selectbox(
                "Select Book ID",
                [b["id"] for b in books],
            )
            selected = find_book(books, selected_id)

            st.warning("Deletion is permanent and cannot be undone.")
            st.write(f"**Book ID:** {selected['id']}")
            st.write(f"**Title:** {selected['title']}")
            st.write(f"**Author:** {selected['author']}")

            confirm = st.checkbox(
                "I confirm that I want to delete this record."
            )

            if st.button("DELETE BOOK", type="primary", use_container_width=True):
                if not confirm:
                    st.warning("Please confirm before deleting.")
                else:
                    response = requests.delete(
                        f"{API_URL}/books/{selected_id}",
                        timeout=5,
                    )
                    if response.status_code in (200, 204):
                        st.success("Book deleted successfully!")
                        st.rerun()
                    else:
                        api_error(response, "Deleting book")
    except requests.RequestException:
        connection_error()


# ==================== 6. SEARCH BOOKS ====================
elif page == "Search Books":
    render_header(
        "Search Books",
        "Find records by title or author.",
        "DISCOVERY",
    )
    try:
        books = fetch_books()
        query = st.text_input(
            "Search catalogue",
            placeholder="Type a title or author...",
        )

        if not books:
            st.info("No records available to search.")
        elif not query.strip():
            st.info("Enter a search keyword.")
        else:
            results = [
                b for b in books
                if query.strip().casefold() in b["title"].casefold()
                or query.strip().casefold() in b["author"].casefold()
            ]
            st.metric("Matching Records", len(results))
            if results:
                render_table(results)
            else:
                st.warning("No matching books found.")
    except requests.RequestException:
        connection_error()


# ==================== 7. STATISTICS ====================
elif page == "Statistics":
    render_header(
        "Library Statistics",
        "Explore catalogue data with charts and summaries.",
        "ANALYTICS",
    )
    try:
        books = fetch_books()
        if not books:
            st.info("Add books to generate statistics.")
        else:
            counts = get_author_counts(books)
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Records", len(books))
            c2.metric("Unique Authors", len(counts))
            c3.metric(
                "Unique Titles",
                len({b["title"].strip().casefold() for b in books}),
            )

            st.subheader("Author Distribution")
            stats_df = pd.DataFrame(
                list(counts.items()),
                columns=["Author", "Book Records"],
            )

            st.vega_lite_chart(
                stats_df,
                {
                    "mark": {
                        "type": "arc",
                        "innerRadius": 70,
                        "stroke": "#FFFFFF",
                        "strokeWidth": 3,
                    },
                    "encoding": {
                        "theta": {
                            "field": "Book Records",
                            "type": "quantitative",
                        },
                        "color": {
                            "field": "Author",
                            "type": "nominal",
                            "scale": {
                                "range": [
                                    "#30231D",
                                    "#8B5E3C",
                                    "#B77945",
                                    "#CDA982",
                                    "#E7D9C8",
                                ]
                            },
                            "legend": {"title": "Author"},
                        },
                        "tooltip": [
                            {"field": "Author", "type": "nominal"},
                            {"field": "Book Records", "type": "quantitative"},
                        ],
                    },
                    "view": {"stroke": None},
                    "background": "#F7F2EA",
                    "width": "container",
                    "height": 350,
                },
                use_container_width=True,
            )

            st.subheader("Author Summary")
            summary = [
                {"Author": name, "Book Records": count}
                for name, count in sorted(
                    counts.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            ]
            st.dataframe(
                pd.DataFrame(summary),
                hide_index=True,
                use_container_width=True,
            )
            st.caption(
                "Issue/return status and fines are not part of the current model."
            )
    except requests.RequestException:
        connection_error()


# ==================== 8. BOOK DETAILS ====================
elif page == "Book Details":
    render_header(
        "Book Details",
        "View an individual book record.",
        "CATALOGUE",
    )
    try:
        books = fetch_books()
        if not books:
            st.info("No book records available.")
        else:
            selected_id = st.selectbox(
                "Select a book",
                [b["id"] for b in books],
            )
            book = find_book(books, selected_id)
            st.subheader(book["title"])
            st.divider()

            c1, c2 = st.columns(2)
            with c1:
                st.caption("BOOK ID")
                st.markdown(f"## {book['id']}")
            with c2:
                st.caption("AUTHOR")
                st.markdown(f"## {book['author']}")

            st.info(
                "ISBN, genre and publication details require additional database fields."
            )
    except requests.RequestException:
        connection_error()


# ==================== 9. ABOUT ====================
elif page == "About":
    render_header(
        "About Library Management System",
        "An application for managing library book records.",
        "PROJECT INFORMATION",
    )
    st.subheader("Project Overview")
    st.write(
        "Library Management System is a web application for maintaining "
        "book records and viewing catalogue statistics."
    )
    st.divider()
    st.subheader("Technology Stack")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### Python")
        st.write("Core programming language")
    with c2:
        st.markdown("### FastAPI")
        st.write("REST API backend")
    with c3:
        st.markdown("### PostgreSQL")
        st.write("Relational database")

    st.divider()
    st.subheader("Features")
    st.markdown("""
    - Dashboard with book statistics
    - Add, view, update and delete book records
    - Search by title or author
    - Author distribution donut chart
    - Book details
    - Input validation and error messages
    """)
    st.info(
        "Login, issue/return, fines and inventory tracking are not implemented."
    )
    st.markdown(
        '<div class="footer">Library Management System | Streamlit + FastAPI + PostgreSQL</div>',
        unsafe_allow_html=True,
    )