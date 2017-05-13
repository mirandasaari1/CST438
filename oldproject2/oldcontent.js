import * as React from 'react';
import { Chatroom } from './Chatroom';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'messages': []
        };
    }

    componentDidMount() {
        Socket.on('all messages', (data) => {
            this.setState({
                'messages': data['messages']
            });
        })
    }

    render() {
        let messages = this.state.messages.map(
            (n, index) => <li key={index}>{n}</li>
        );
        return (
            <div>
                <h1>Chat List:</h1>
                <ul>{messages}</ul>
                <Button />
            </div>
        );
    }
}
