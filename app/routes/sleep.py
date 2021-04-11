from flask import render_template

from app.routes import bp
from random import uniform
from time import sleep


@bp.route('/sleep', defaults={'duration': '0', 'probability': '100'})
@bp.route('/sleep/<int:duration>', defaults={'probability': '100'})
@bp.route('/sleep/<int:duration>/<int:probability>')
def simulate_sleep(duration, probability):
    # sleep for duration seconds.
    status_code_ = 200  # OK
    probability_int = int(probability)
    try:
        assert 0 <= probability_int <= 100
        # continue processing
    except AssertionError:
        # set probability to %100
        probability_int = 100
        status_code_ = 400  # Bad Request
    duration_float = float(duration)
    try:
        assert 0 <= duration_float <= 60
        # continue processing
    except AssertionError:
        # set duration to 0 seconds
        duration_float = 0
        status_code_ = 400  # Bad Request
    do_sleep_action = True
    action_message_ = 'SKIPPED'
    if probability_int != 100:
        p = uniform(0, 100)
        do_sleep_action = probability_int >= p
    if do_sleep_action:
        action_message_ = 'SUCCESSFUL'
        sleep(duration_float)
    message_ = "Simulating website with %{probability_p} delay of {duration_s} seconds".format(
        duration_s=duration_float,
        probability_p=probability_int
    )
    return render_template(
        'base_layout.html',
        message=message_,
        status_code=status_code_,
        action_message=action_message_
    ), status_code_

