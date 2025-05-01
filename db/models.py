from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    zodiac_sign = Column(String, nullable=True)
    preferred_temperature_unit = Column(String, nullable=False, default='Celsius')
    last_login = Column(DateTime, nullable=True)

class Location(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    is_primary = Column(Boolean, default=False)
    user = relationship('User', back_populates='locations')

User.locations = relationship('Location', order_by=Location.location_id, back_populates='user')

class WeatherForecast(Base):
    __tablename__ = 'weather_forecasts'
    forecast_id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.location_id'), nullable=False)
    forecast_date = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    condition = Column(String, nullable=False)
    wind_speed = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    precipitation = Column(Float, nullable=True)
    is_hourly = Column(Boolean, default=False)
    location = relationship('Location', back_populates='forecasts')

Location.forecasts = relationship('WeatherForecast', order_by=WeatherForecast.forecast_id, back_populates='location')

class WeatherAlert(Base):
    __tablename__ = 'weather_alerts'
    alert_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    alert_type = Column(String, nullable=False)
    condition_trigger = Column(String, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True)
    user = relationship('User', back_populates='alerts')

User.alerts = relationship('WeatherAlert', order_by=WeatherAlert.alert_id, back_populates='user')

class CustomAlertPreference(Base):
    __tablename__ = 'custom_alert_preferences'
    preference_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    activity = Column(String, nullable=False)
    temperature_threshold = Column(Float, nullable=True)
    wind_threshold = Column(Float, nullable=True)
    enabled = Column(Boolean, default=True)
    user = relationship('User', back_populates='custom_alert_preferences')

User.custom_alert_preferences = relationship('CustomAlertPreference', order_by=CustomAlertPreference.preference_id, back_populates='user')

class Horoscope(Base):
    __tablename__ = 'horoscopes'
    horoscope_id = Column(Integer, primary_key=True)
    zodiac_sign = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    general_prediction = Column(String, nullable=False)
    weather_insight = Column(String, nullable=True)

class HoroscopeShare(Base):
    __tablename__ = 'horoscope_shares'
    share_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    horoscope_id = Column(Integer, ForeignKey('horoscopes.horoscope_id'), nullable=False)
    shared_at = Column(DateTime, nullable=False)
    platform = Column(String, nullable=False)
    user = relationship('User', back_populates='horoscope_shares')
    horoscope = relationship('Horoscope', back_populates='shares')

User.horoscope_shares = relationship('HoroscopeShare', order_by=HoroscopeShare.share_id, back_populates='user')
Horoscope.shares = relationship('HoroscopeShare', order_by=HoroscopeShare.share_id, back_populates='horoscope')

class AppSetting(Base):
    __tablename__ = 'app_settings'
    setting_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    show_tips = Column(Boolean, default=True)
    notification_sound = Column(String, nullable=True)
    time_window_start = Column(DateTime, nullable=True)
    time_window_end = Column(DateTime, nullable=True)
    override_settings_for_emergency = Column(Boolean, default=False)
    user = relationship('User', back_populates='app_settings')

User.app_settings = relationship('AppSetting', order_by=AppSetting.setting_id, back_populates='user')