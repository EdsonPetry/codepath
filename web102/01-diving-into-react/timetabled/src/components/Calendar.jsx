import Event from "./Event"

const Calendar = () => {
    
    return (
        <div className="Calendar">
            <table>
                <tr>
                <th></th>
                    <th>Sunday</th>
                    <th>Monday</th>
                    <th>Tuesday</th>
                    <th>Wednesday</th>
                    <th>Thursday</th>
                    <th>Friday</th>
                    <th>Saturday</th>
                </tr>
                <tbody>
                    <tr>
                        <td className="time">8 am</td>
                        <Event event="Fancy Dinner 🎩" color="green" location="123 Street rd." />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">9 am</td>
                        <Event />
                        <Event />
                        <Event event='The Bean 🫘' color ='blue'/>
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">10 am</td>
                        <Event />
                        <Event />
                        <Event event="Yolk 🍳" color="green" />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">11 am</td>
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">12 pm</td>
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">1 pm</td>
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">2 pm</td>
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">3 pm</td>
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">4 pm</td>
                        <Event />
                        <Event />
                        <Event />
                        <Event event='Starbucks ☕️' color ='green'/>
                        <Event />
                        <Event />
                        <Event />
                    </tr>
                    <tr>
                        <td className="time">5 pm</td>
                        <Event />
                        <Event />
                        <Event event='Subway 🚊' color ='pink'/>
                        <Event />
                        <Event />
                        <Event />
                        <Event event='The Bean 🫘' color ='blue'/>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}

export default Calendar