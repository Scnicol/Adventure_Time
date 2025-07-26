import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { useHistory } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { useModal } from "../../context/Modal";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const { setModalContent, closeModal } = useModal();

  const handleLogout = async (e) => {
    e.preventDefault();
    await dispatch(logout());
    closeModal();
    history.push("/");
  };

  const openProfileModal = () => {
    setModalContent(
      <div className="profile-modal-content">
        {user ? (
          <>
            <div style={{ marginBottom: 12, fontWeight: 600 }}>{user.username}</div>
            <button className="profile-btn" onClick={handleLogout} style={{ width: '100%' }}>Log Out</button>
          </>
        ) : (
          <>
            <OpenModalButton
              buttonText="Log In"
              onItemClick={closeModal}
              modalComponent={<LoginFormModal />}
              className="profile-modal-nav-btn"
            />
            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeModal}
              modalComponent={<SignupFormModal />}
              className="profile-modal-nav-btn"
            />
          </>
        )}
      </div>
    );
  };

  return (
    <button className="profile-btn" onClick={openProfileModal}>
      <i className="fas fa-user-circle" />
    </button>
  );
}

export default ProfileButton;
