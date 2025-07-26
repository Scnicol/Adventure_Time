import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<nav className="nav-bar-flex">
			<div className="nav-left">
				<ul>
					<li>
						<NavLink exact to="/">Home</NavLink>
					</li>
					<li>
						<ProfileButton user={sessionUser} />
					</li>
				</ul>
			</div>
			<div className="nav-right">
				<ul>
					{sessionUser && (
						<>
							<li>
								<NavLink to="/my-adventures">My Adventures</NavLink>
							</li>
							<li>
								<NavLink to="/activities">Activities</NavLink>
							</li>
							<li>
								<NavLink to="/food">Food</NavLink>
							</li>
						</>
					)}
				</ul>
			</div>
		</nav>
	);
}

export default Navigation;
