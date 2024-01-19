import datetime


class ConferenceRoom:
    def __init__(self, id, offices, reservations, part_times):
        self.id = id
        self.offices = offices
        self.reservations = reservations
        self.part_times = part_times

    @classmethod
    def formatting(cls, id, offices, reservations, part_times):
        if part_times:
            for part_time in part_times:
                seconds = part_time['time'].seconds
                part_time['time'] = str(datetime.timedelta(seconds=seconds))

        if reservations:
            for reservation in reservations:
                reservation_seconds = reservation['time'].seconds
                reservation['time'] = str(datetime.timedelta(seconds=reservation_seconds))
                reservation['created_date'] = reservation['created_date'].strftime("%Y-%m-%d %H:%M")

        if len(reservations) <= len(part_times):
            for reservation in reservations:
                for index, part_time in enumerate(part_times):
                    if reservation['time'] == part_time['time']:
                        del part_times[index]

        return cls(id, offices, reservations, part_times)
