"""
HTML Report Generator
Version 1.0
"""

from datetime import datetime
import os


class ReportGenerator:

    def __init__(self):

        self.template = "reports/template.html"

        self.output_folder = "reports/output"

        os.makedirs(

            self.output_folder,

            exist_ok=True,

        )

    def generate(

        self,

        decision,

        portfolio,

        trade,

        ai_stats,

        backtest,

    ):

        with open(

            self.template,

            "r",

            encoding="utf-8",

        ) as file:

            html = file.read()

        content = f"""

<h1>AI Investment Agent Report</h1>

<div class="card">

<h2>Decision</h2>

<table>

<tr><td>Recommendation</td><td>{decision['recommendation']}</td></tr>

<tr><td>Confidence</td><td>{decision['confidence']}%</td></tr>

<tr><td>Position</td><td>{decision['position']}</td></tr>

<tr><td>Holding</td><td>{decision['holding']}</td></tr>

</table>

</div>

<div class="card">

<h2>Portfolio</h2>

<table>

"""

        for item in portfolio["allocation"]:

            content += f"""

<tr>

<td>{item['asset']}</td>

<td>{item['percent']}%</td>

<td>{item['amount']:,}</td>

</tr>

"""

        content += """

</table>

</div>

"""

        if trade:

            content += f"""

<div class="card">

<h2>Current Trade</h2>

<table>

<tr><td>Asset</td><td>{trade['asset']}</td></tr>

<tr><td>Signal</td><td>{trade['signal']}</td></tr>

<tr><td>Entry</td><td>{trade['entry']}</td></tr>

<tr><td>Stop Loss</td><td>{trade['stop_loss']}</td></tr>

<tr><td>Take Profit</td><td>{trade['take_profit']}</td></tr>

</table>

</div>

"""

        content += f"""

<div class="card">

<h2>AI Experience</h2>

<table>

<tr><td>Experience</td><td>{ai_stats['experience']}</td></tr>

<tr><td>Wins</td><td>{ai_stats['wins']}</td></tr>

<tr><td>Losses</td><td>{ai_stats['losses']}</td></tr>

<tr><td>Win Rate</td><td>{ai_stats['confidence']}%</td></tr>

</table>

</div>

<div class="card">

<h2>Backtest</h2>

<table>

<tr><td>Total Trades</td><td>{backtest['trades']}</td></tr>

<tr><td>Wins</td><td>{backtest['wins']}</td></tr>

<tr><td>Losses</td><td>{backtest['losses']}</td></tr>

<tr><td>Win Rate</td><td>{backtest['win_rate']}%</td></tr>

<tr><td>Total PnL</td><td>{backtest['total_pnl']}</td></tr>

</table>

</div>

"""

        html = html.replace(

            "{{CONTENT}}",

            content,

        )

        filename = datetime.now().strftime(

            "report_%Y%m%d_%H%M%S.html"

        )

        output = os.path.join(

            self.output_folder,

            filename,

        )

        with open(

            output,

            "w",

            encoding="utf-8",

        ) as file:

            file.write(html)

        return output