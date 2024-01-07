import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entrance for the main project.")

    # Subparsers for different commands
    subparsers = parser.add_subparsers(title="Available commands", dest="command")

    # Command: run
    run_parser = subparsers.add_parser("run", help="Run the program with a specified front-end framework.")
    run_parser.add_argument("-f", "--framework", choices=["tkinter", "pyQt"], default="tkinter",
                            help="Specify the front-end framework (tkinter or pyQt).")
    run_parser.add_argument("-u", "--uid", nargs="?", default="0", help="Specify the user's UID (default is '0').")

    # Command: stimulator
    stimulator_parser = subparsers.add_parser("stimulator", help="Generate simulated data.")
    stimulator_parser.add_argument("-d", "--data_type",
                                   choices=["a", "all", "s", "step", "d", "distance", "f", "floor", "ah",
                                            "active_hours", "ae", "active_energy", "em", "exercise_minutes"],
                                   help="Specify the type of data to generate.")
    stimulator_parser.add_argument("uid", nargs="?", default="0", help="Specify the user's UID (default is '0').")

    args = parser.parse_args()

    if args.command == "run":
        print(f"Running with {args.framework} framework.")

        if args.framework == "tkinter":
            from health_tracker.health_app_tkinter import *
            run_app(user_id=args.uid)
        elif args.framework == "pyQt":
            from health_tracker.health_app_pyqt import *
            run_app(user_id=args.uid)
        else:
            raise ValueError(f"Unknown framework: {args.framework}")

    elif args.command == "stimulator":
        print(f"Generating data {args.data_type} for user {args.uid}.")

        from health_tracker.tracker import *
        if args.data_type == "a" or args.data_type == "all":  # 生成所有数据
            DataStimulator.stimulate_all_data(args.uid)
        elif args.data_type == "s" or args.data_type == "step":  # 生成步数数据
            DataStimulator.stimulate_step_count(args.uid)
        elif args.data_type == "d" or args.data_type == "distance":  # 生成距离数据
            DataStimulator.stimulate_distance(args.uid)
        elif args.data_type == "f" or args.data_type == "floor":  # 生成爬楼数据
            DataStimulator.stimulate_flights_climbed(args.uid)
        elif args.data_type == "ah" or args.data_type == "active_hours":  # 生成活动时间数据
            DataStimulator.stimulate_active_hours(args.uid)
        elif args.data_type == "ae" or args.data_type == "active_energy":  # 生成活动热量数据
            DataStimulator.stimulate_active_energy_burned(args.uid)
        elif args.data_type == "em" or args.data_type == "exercise_minutes":  # 生成运动时间数据
            DataStimulator.stimulate_exercise_minutes(args.uid)
        else:
            raise ValueError(f"Unknown data type: {args.data_type}")

    else:
        parser.print_help()
