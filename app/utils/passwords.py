
import bcrypt


class PasswordEncoder:
    def encodePassword(self, password: str) -> str:
        passBytes = password.encode()
        hashedPasswordAsBytes = bcrypt.hashpw(passBytes, bcrypt.gensalt(14))
        hashedPassword = hashedPasswordAsBytes.decode()
        return hashedPassword
    
    def comparePassword(self, password:str, hashedPassword:str) -> bool:
        passwordUserInputBytes = password.encode()
        passwordBytes = hashedPassword.encode()
        return bcrypt.checkpw(passwordUserInputBytes, passwordBytes)