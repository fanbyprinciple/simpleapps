import React from 'react'
import { Link } from 'react-router'

export default class AthletesMenu extends React.Component {
    render() {
        return (
            <nav className="athletes-menu">
                {this.props.athletes.map(menuAthlete => {
                    return <Link key={menuAthlete.id} to={`/athlete/${menuAthlete.id}`} activeClassName="active"> {menuAthlete.name} </Link>
                })}
            </nav>
        )
    }
}

/*
We are expecting the data to be passed in the component through a athletes prop. So from the outside, when we use the component in our layout, we will need to propagate the list of athletes available in the app directly into the component.
We use the map method to iterate over all the athletes and generate for every one of them a Link.
Link is a special component provided by React Router to create links between views.
Finally, we use the prop activeClassName to use the class active when the current route matches the path of the link.
*/ 
