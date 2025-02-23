
const Event = ({ event, color, location }) => {

    return (
        <>
            <td className={"Event " + color}>
                <h5>{event}</h5>
                <h6>{location}</h6>
            </td>
        </>
    )
}


export default Event;