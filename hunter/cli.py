import argparse
from .models import Target
from .passive import hunt, report_json

def main() -> None:
    parser = argparse.ArgumentParser(description="Scope-first, non-destructive bug hunter")
    parser.add_argument("--target", required=True, help="Explicitly authorized in-scope http(s) URL")
    parser.add_argument("--name", default="target")
    args = parser.parse_args()
    print(report_json(hunt(Target(name=args.name, base_url=args.target, in_scope=True))))

if __name__ == "__main__":
    main()
