import sys
from analytics import Research, Analytics
import config

def main():
    if len(sys.argv) != 2:
        print("юзай python make_report.py data.csv")
        sys.exit(1)

    path = sys.argv[1]


    research = Research(path)
    data = research.file_reader()

    analytics = Analytics(data)
    heads, tails = analytics.counts()
    heads_perc, tails_perc = analytics.fractions(heads, tails)


    preds = analytics.predict_random(config.num_of_steps)
    pred_heads = sum(1 for p in preds if p == [1, 0])
    pred_tails = sum(1 for p in preds if p == [0, 1])

   
    report_text = config.report_template.format(
        total=len(data),
        heads=heads,
        tails=tails,
        heads_perc=heads_perc,
        tails_perc=tails_perc,
        num_steps=config.num_of_steps,
        pred_heads=pred_heads,
        pred_tails=pred_tails
    )

   
    filename = analytics.save_file(report_text, "report", "txt")
    print(f"Report saved to {filename}")


if __name__ == "__main__":
    main()
