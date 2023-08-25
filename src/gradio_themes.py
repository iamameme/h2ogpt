from __future__ import annotations

from typing import Iterable

from gradio.themes.soft import Soft
from gradio.themes import Color, Size
from gradio.themes.utils import colors, sizes, fonts

h2o_yellow = Color(
    name="yellow",
    c50="#fffef2",
    c100="#fff9e6",
    c200="#ffecb3",
    c300="#ffe28c",
    c400="#ffd659",
    c500="#d1363a",
    c600="#e6ac00",
    c700="#bf8f00",
    c800="#a67c00",
    c900="#664d00",
    c950="#403000",
)
h2o_gray = Color(
    name="gray",
    c50="#f8f8f8",
    c100="#e5e5e5",
    c200="#cccccc",
    c300="#b2b2b2",
    c400="#999999",
    c500="#7f7f7f",
    c600="#666666",
    c700="#4c4c4c",
    c800="#333333",
    c900="#191919",
    c950="#0d0d0d",
)


text_xsm = Size(
    name="text_xsm",
    xxs="4px",
    xs="5px",
    sm="6px",
    md="7px",
    lg="8px",
    xl="10px",
    xxl="12px",
)


spacing_xsm = Size(
    name="spacing_xsm",
    xxs="1px",
    xs="1px",
    sm="1px",
    md="2px",
    lg="3px",
    xl="5px",
    xxl="7px",
)


radius_xsm = Size(
    name="radius_xsm",
    xxs="1px",
    xs="1px",
    sm="1px",
    md="2px",
    lg="3px",
    xl="5px",
    xxl="7px",
)


class H2oTheme(Soft):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = h2o_yellow,
            secondary_hue: colors.Color | str = h2o_yellow,
            neutral_hue: colors.Color | str = h2o_gray,
            spacing_size: sizes.Size | str = sizes.spacing_md,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_lg,
            font: fonts.Font
            | str
            | Iterable[fonts.Font | str] = (
                fonts.GoogleFont("Montserrat"),
                "ui-sans-serif",
                "system-ui",
                "sans-serif",
            ),
            font_mono: fonts.Font
            | str
            | Iterable[fonts.Font | str] = (
                fonts.GoogleFont("IBM Plex Mono"),
                "ui-monospace",
                "Consolas",
                "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            link_text_color="#3344DD",
            link_text_color_hover="#3344DD",
            link_text_color_visited="#3344DD",
            link_text_color_dark="#74abff",
            link_text_color_hover_dark="#a3c8ff",
            link_text_color_active_dark="#a3c8ff",
            link_text_color_visited_dark="#74abff",
            button_primary_text_color="*neutral_950",
            button_primary_text_color_dark="*neutral_950",
            button_primary_background_fill="#d1363a",
            button_primary_background_fill_dark="*primary_500",
            block_label_background_fill="*primary_500",
            block_label_background_fill_dark="*primary_500",
            block_label_text_color="*neutral_950",
            block_label_text_color_dark="*neutral_950",
            block_title_text_color="*neutral_950",
            block_title_text_color_dark="*neutral_950",
            block_background_fill_dark="*neutral_950",
            body_background_fill="*neutral_50",
            body_background_fill_dark="*neutral_900",
            background_fill_primary_dark="*block_background_fill",
            block_radius="0 0 8px 8px",
            checkbox_label_text_color_selected_dark='#000000',
            #checkbox_label_text_size="*text_xs",  # too small for iPhone etc. but good if full large screen zoomed to fit
            checkbox_label_text_size="*text_sm",
            #radio_circle="""url("data:image/svg+xml,%3csvg viewBox='0 0 32 32' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3ccircle cx='32' cy='32' r='1'/%3e%3c/svg%3e")""",
            #checkbox_border_width=1,
            #heckbox_border_width_dark=1,
        )


class SoftTheme(Soft):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = colors.indigo,
            secondary_hue: colors.Color | str = colors.indigo,
            neutral_hue: colors.Color | str = colors.gray,
            spacing_size: sizes.Size | str = sizes.spacing_md,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_md,
            font: fonts.Font
            | str
            | Iterable[fonts.Font | str] = (
                fonts.GoogleFont("Montserrat"),
                "ui-sans-serif",
                "system-ui",
                "sans-serif",
            ),
            font_mono: fonts.Font
            | str
            | Iterable[fonts.Font | str] = (
                fonts.GoogleFont("IBM Plex Mono"),
                "ui-monospace",
                "Consolas",
                "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            checkbox_label_text_size="*text_sm",
        )


h2o_logo = '<svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"' \
           ' viewBox="0 0 600.28 600.28"><defs><style>.cls-1{fill:#fec925;}.cls-2{fill:#161616;}.cls-3{fill:' \
           '#54585a;}</style></defs><g id="Fill-1"><rect class="cls-1" width="600.28" height="600.28" ' \
           'rx="23.24"/></g><path class="cls-2" d="M174.33,246.06v92.78H152.86v-38H110.71v38H89.24V246.06h21.' \
           '47v36.58h42.15V246.06Z"/><path class="cls-2" d="M259.81,321.34v17.5H189.7V324.92l35.78-33.8c8.22-7.' \
           '82,9.68-12.59,9.68-17.09,0-7.29-5-11.53-14.85-11.53-7.95,0-14.71,3-19.21,9.27L185.46,261.7c7.15-10' \
           '.47,20.14-17.23,36.84-17.23,20.68,0,34.46,10.6,34.46,27.44,0,9-2.52,17.22-15.51,29.29l-21.33,20.14Z"' \
           '/><path class="cls-2" d="M268.69,292.45c0-27.57,21.47-48,50.76-48s50.76,20.28,50.76,48-21.6,48-50.' \
           '76,48S268.69,320,268.69,292.45Zm79.78,0c0-17.63-12.46-29.69-29-29.69s-29,12.06-29,29.69,12.46,29.69' \
           ',29,29.69S348.47,310.08,348.47,292.45Z"/><path class="cls-3" d="M377.23,326.91c0-7.69,5.7-12.73,12.' \
           '85-12.73s12.86,5,12.86,12.73a12.86,12.86,0,1,1-25.71,0Z"/><path class="cls-3" d="M481.4,298.15v40.' \
           '69H462.05V330c-3.84,6.49-11.27,9.94-21.74,9.94-16.7,0-26.64-9.28-26.64-21.61,0-12.59,8.88-21.34,30.' \
           '62-21.34h16.43c0-8.87-5.3-14-16.43-14-7.55,0-15.37,2.51-20.54,6.62l-7.43-14.44c7.82-5.57,19.35-8.' \
           '62,30.75-8.62C468.81,266.47,481.4,276.54,481.4,298.15Zm-20.68,18.16V309H446.54c-9.67,0-12.72,3.57-' \
           '12.72,8.35,0,5.16,4.37,8.61,11.66,8.61C452.37,326,458.34,322.8,460.72,316.31Z"/><path class="cls-3"' \
           ' d="M497.56,246.06c0-6.49,5.17-11.53,12.86-11.53s12.86,4.77,12.86,11.13c0,6.89-5.17,11.93-12.86,' \
           '11.93S497.56,252.55,497.56,246.06Zm2.52,21.47h20.68v71.31H500.08Z"/></svg>'


def get_h2o_title(title, description):
    # NOTE: Check full width desktop, smallest width browser desktop, iPhone browsers to ensure no overlap etc.
    return f"""<div style="float:left; justify-content:left; height: 80px; width: 195px; margin-top:0px">
                    
                </div>
                <div style="display:flex; justify-content:center; margin-bottom:30px; margin-right:330px;">
                    <div style="height: 60px; width: 80px; margin-right:20px; fill: #f9f9f9; margin-top: 15px;">
                    <svg width="85" height="27" class="_32ANSIZormifc9Vc6VVwrx" viewBox="0 0 587.93 165" style="color: white;"><title>mainLogoRiotFist21</title><path d="M98.77.33L0 46.07l24.61 93.66 18.73-2.3-5.15-58.89 6.15-2.74L54.96 136l32.01-3.93-5.69-65 6.09-2.71 11.68 66.23 32.38-3.98-6.23-71.25 6.16-2.74 12.77 72.43 32.01-3.93V19.71L98.77.33zm2.32 142.05l1.63 9.22 73.42 12.24v-30.68l-75.01 9.22h-.04zm144.49-19.22v12.63h15.57a14.84 14.84 0 01-1.92 7.31 13 13 0 01-5.6 5.11 20 20 0 01-8.9 1.8 17.53 17.53 0 01-10-2.8 17.87 17.87 0 01-6.44-8.14 33.06 33.06 0 01-2.27-12.93 31.81 31.81 0 012.32-12.81 18.14 18.14 0 016.5-8 17.27 17.27 0 019.82-2.78 19.31 19.31 0 015.36.71 14.15 14.15 0 014.33 2.09 12.92 12.92 0 013.18 3.29 15.61 15.61 0 012 4.44h17.27a27.22 27.22 0 00-3.46-10.28 28.84 28.84 0 00-7.05-8.1 32.6 32.6 0 00-9.91-5.29 37.91 37.91 0 00-12.06-1.86 37.32 37.32 0 00-14 2.6 32.6 32.6 0 00-11.36 7.61 35 35 0 00-7.61 12.21 46.15 46.15 0 00-2.73 16.44q0 11.94 4.54 20.59a32.4 32.4 0 0012.69 13.27 39.84 39.84 0 0035.84.84 28.39 28.39 0 0011.67-11q4.25-7.19 4.24-17.2v-9.76zm215.03 40.81V88.53h51.67v13.96h-34.62v16.76h27.99v13.96h-27.99v16.8h34.7v13.96h-51.75zm101.83-53.3a9 9 0 00-3.54-6.64c-2.09-1.59-5-2.38-8.69-2.38a16.63 16.63 0 00-6.26 1 8.62 8.62 0 00-3.83 2.78 6.74 6.74 0 00-1.33 4 6.2 6.2 0 00.79 3.29 7.27 7.27 0 002.4 2.45 16.54 16.54 0 003.7 1.79 40.14 40.14 0 004.64 1.31l6.63 1.54a47.19 47.19 0 019.45 3.08 27.46 27.46 0 017.2 4.68 18.84 18.84 0 014.58 6.39 20.37 20.37 0 011.61 8.29 20.65 20.65 0 01-3.54 12.11 22.56 22.56 0 01-10.15 7.85 41.31 41.31 0 01-15.93 2.76 42.69 42.69 0 01-16.17-2.81 23.22 23.22 0 01-10.72-8.48q-3.83-5.66-4-14.12h16.43a10.68 10.68 0 007.05 9.94 19.37 19.37 0 007.24 1.26 18.44 18.44 0 006.66-1.09 10 10 0 004.33-3 7.22 7.22 0 001.57-4.48 6.16 6.16 0 00-1.42-4 10.86 10.86 0 00-4.14-2.81 42.07 42.07 0 00-6.89-2.14l-8.07-1.95q-9.65-2.3-15.23-7.26t-5.54-13.44a19.86 19.86 0 013.72-12.12 24.74 24.74 0 0110.33-8.11 36.74 36.74 0 0115-2.91 35.62 35.62 0 0114.92 2.91 23.43 23.43 0 019.91 8.14 21.54 21.54 0 013.6 12.12zm-113.99 53.3h-16.87v-57.35l-1.73-.02-17.04 57.37h-16.86l-16.58-57.37-2.15.02v57.35h-16.87V88.53h28.67l14.48 50.56h1.75l14.48-50.56h28.72v75.44zm-114.66 0h18.27l-25.33-75.43h-23.15l-25.37 75.43h18.3l4.93-16.54h27.42zm-28.43-29.7l8.22-27.65h3.1l8.26 27.65zm278.58-37.76a4 4 0 01-3.67-2.44 4 4 0 010-3.1 4 4 0 01.85-1.27 4.25 4.25 0 011.27-.86 4.15 4.15 0 013.1 0 4.13 4.13 0 011.27.86 4.08 4.08 0 01.86 1.27 4 4 0 010 3.1 4.08 4.08 0 01-.86 1.27 4 4 0 01-1.27.86 4 4 0 01-1.55.31zm0-1.09a2.84 2.84 0 001.47-.39 2.94 2.94 0 001.05-1 2.93 2.93 0 000-2.92 3 3 0 00-1.06-1 2.93 2.93 0 00-2.92 0 3 3 0 00-1 1 2.86 2.86 0 000 2.92 3 3 0 001 1 2.83 2.83 0 001.46.39zm-1.46-1.15V90.6h1.78a1.52 1.52 0 01.69.15 1.13 1.13 0 01.47.42 1.24 1.24 0 01.17.66 1.16 1.16 0 01-.18.66 1 1 0 01-.48.41 1.56 1.56 0 01-.7.14h-1.2v-.72h1a.52.52 0 00.36-.12.5.5 0 00.14-.37.47.47 0 00-.14-.37.52.52 0 00-.36-.12h-.55v2.93zm2.39-1.68l.82 1.68h-1.11l-.75-1.68zM282.41 1.03h17.05v75.44h-17.05zm98.02 37.72q0 12.42-4.71 21a32.67 32.67 0 01-12.79 13.17 38.57 38.57 0 01-36.31 0 32.75 32.75 0 01-12.79-13.2q-4.71-8.66-4.71-21t4.71-21.05a32.67 32.67 0 0112.75-13.14 38.65 38.65 0 0136.31 0 32.67 32.67 0 0112.79 13.17q4.71 8.64 4.71 21.05m-17.35 0a33.35 33.35 0 00-2.23-13 17.47 17.47 0 00-6.33-8 18.57 18.57 0 00-19.45 0 17.57 17.57 0 00-6.35 8 38.59 38.59 0 000 26 17.49 17.49 0 006.35 8 18.57 18.57 0 0019.45 0 17.39 17.39 0 006.33-8 33.4 33.4 0 002.23-13M246.58 50.17l8.76 26.3h18.71l-9.74-28.33h-13.23l-.79-2.44c2.52-.49 6.83-1.25 10.65-3.85a20 20 0 008.75-16.39 24.15 24.15 0 00-3.26-12.75 21.9 21.9 0 00-9.36-8.64 32.56 32.56 0 00-14.64-3H212v75.4h17.06v-26.3zm-.32-15.61a19.35 19.35 0 01-7.26 1.18h-9.94V14.88h9.91a18.68 18.68 0 017.25 1.24 9.12 9.12 0 014.4 3.7 10 10 0 011.5 5.64 9.65 9.65 0 01-1.48 5.55 8.86 8.86 0 01-4.38 3.55M382.04 1.03v14h29.3l.8 2.45c-2.48.48-6.67 1.22-10.43 3.7v55.31h16.87v-61.5h19.62v-14z" style="color: white;"></path></svg>
                    </div>
                    <h1 style="line-height:60px">Test Riotnet ITDND GPT</h1>
                </div>
                <div style="float:right; height: 80px; width: 80px; margin-top:-100px">
                    <img src="">
                </div>
                """


def get_simple_title(title, description):
    return f"""{description}<h1 align="center"> {title}</h1>"""


def get_dark_js() -> str:
    return """
        if (document.querySelectorAll('.dark').length) {
            document.querySelectorAll('.dark').forEach(el => el.classList.remove('dark'));
        } else {
            document.querySelector('body').classList.add('dark');
        }
    """

def get_heap_js(heapAppId: str) -> str:
    return ("""globalThis.window.heap=window.heap||[],heap.load=function(e,t){window.heap.appid=e,window.heap.config=t=t||{};var r=document.createElement("script");r.type="text/javascript",r.async=!0,r.src="https://cdn.heapanalytics.com/js/heap-"+e+".js";var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(r,a);for(var n=function(e){return function(){heap.push([e].concat(Array.prototype.slice.call(arguments,0)))}},p=["addEventProperties","addUserProperties","clearEventProperties","identify","resetIdentity","removeEventProperty","setEventProperties","track","unsetEventProperty"],o=0;o<p.length;o++)heap[p[o]]=n(p[o])};"""
           f"""heap.load("{heapAppId}");""")

def wrap_js_to_lambda(*args: str) -> str:
    newline = "\n"
    return f"""
        () => {{
            {newline.join([a for a in args if a is not None])}
        }}
    """
