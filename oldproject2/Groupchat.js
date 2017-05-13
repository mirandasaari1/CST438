import * as React from 'react';

import { Socket } from './Socket';

export class Groupchat extends React.Component {
    handleSubmit(event) {
        event.preventDefault();

        let random = Math.floor(Math.random() * 100);
        console.log('Generated a random message: ', random);
        Socket.emit('new message', {
            'message': random,
        });
        console.log('Sent up the random message to server!');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Send up a random message!</button>
            </form>
        );
    }
}