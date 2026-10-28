class ParkingPermit:
    def __init__(self, name: str, months: int, fee_sched: dict):
        self.owner_name = name
        self.months_purchased = months
        self.fee_schedule = fee_sched

class StudentPermit(ParkingPermit):
    def __init__(self, name: str, months: int, fee_sched: dict, vehicles: int):
        ParkingPermit.__init__(self, name, months, fee_sched)
        self.vehicle_count = vehicles
    
    def cost(self):
        """student permit costs $25 per month plus one time $10 fee
        for each vehicle after first"""
        return (self.fee_schedule['monthly'] * self.months_purchased
                + self.fee_schedule['additional_vehicle'] * self.vehicle_count)
    
    def __str__(self):
        return (
            f'Student Permit | Name: {self.owner_name} | '
            f'Duration: {self.months_purchased} months | '
            f'{self.vehicle_count} vehicle'
            f'{'s' if self.vehicle_count > 1 else ''}'
        )
    
    def __repr__(self):
        return (
            f'student name: {self.owner_name}, '
            f'duration: {self.months_purchased} months, '
            f'vehicle count: {self.vehicle_count}, cost: {self.cost()}'
        )

class FacultyPermit(ParkingPermit):
    def __init__(self, name: str, months: int, fee_sched: dict,
                 garage_acc: bool):
        ParkingPermit.__init__(self, name, months, fee_sched)
        self.garage_access = garage_acc
        
    def cost(self):
        """faculty permit costs $40 per month plus one time $15 fee
        per month for garage access"""
        if self.garage_access:
            return (self.fee_schedule['monthly'] * self.months_purchased
                    + self.fee_schedule['garage'])
        else:
            return (self.fee_schedule['monthly'] * self.months_purchased)
    
    def __str__(self):
        return (
            f'Faculty Permit | Name: {self.owner_name} | '
            f'Duration: {self.months_purchased} months'
            f'{' | Garage access' if self.garage_access else ''}'
        )
    
    def __repr__(self):
        return (
            f'faculty name: {self.owner_name}, '
            f'duration: {self.months_purchased} months, '
            f'garage access: {self.garage_access}, cost: {self.cost()}'
        )

student_fees = {
    'monthly': 25.00,
    'additional_vehicle': 10.00
}

faculty_fees = {
    'monthly': 40.00,
    'garage': 15.00
}

def summarize_list(permit_list):
    revenue = 0
    
    for permit in permit_list:
        print(f'{str(permit)} | Cost: {permit.cost()}')
        revenue += permit.cost()
    
    return revenue

def main():
    john = StudentPermit('John Frank', 8, student_fees, 2)
    bill = FacultyPermit('Billy Austin', 50, faculty_fees, True)
    
    print(summarize_list([john, bill]))

if __name__ == '__main__':
    main()