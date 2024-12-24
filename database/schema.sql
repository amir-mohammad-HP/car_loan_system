USE car_loan;


CREATE TABLE ManageCar (
    staff_uid UNIQUEIDENTIFIER,
    car_uid UNIQUEIDENTIFIER,
    PRIMARY KEY (staff_uid, car_uid),
    FOREIGN KEY (staff_uid) REFERENCES Staffs(uid),
    FOREIGN KEY (car_uid) REFERENCES Cars(uid)
);

CREATE TABLE Reservations (
    customer_uid UNIQUEIDENTIFIER,
    car_uid UNIQUEIDENTIFIER,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) CHECK (
        status IN (
            'Pending',
            'Active',
            'Completed',
            'Cancelled'
        )
    ) DEFAULT'Active',
    PRIMARY KEY (customer_uid, car_uid),
    FOREIGN KEY (customer_uid) REFERENCES Customers(uid),
    FOREIGN KEY (car_uid) REFERENCES Cars(uid)
);

CREATE TABLE Logs (
    id INT IDENTITY (1, 1),
    message TEXT,
    level VARCHAR(20) CHECK (
        level IN (
            'INFO',
            'DEBUG',
            'WARNING',
            'ERROR'
        )
    ),
    created_at DATETIME DEFAULT GETDATE(),
);