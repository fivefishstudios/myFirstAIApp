To create high-quality layer-separated prompts in ChatGPT, follow these guidelines:

    Break the description into multiple layers, focusing on distinct aspects of the subject.

    Assign weights to each layer (::X, where X is a number) based on the importance or prominence of that aspect. Use the dynamic range of layer weights, with only one or two important layers having high weights, a few having medium weights, and the rest having low weights.

    Negative weights can be used as a way to negate unwanted subjects or aspects, but keep in mind that the total layer weight can never be negative.

    Adjust the weights to ensure the desired emphasis is achieved in the final result. If a prompt doesn't produce the desired results, experiment with adjusting the layer weights until you achieve the desired balance.

    Keep tokens in layers congruous and supportive; avoid mixing different ideas within one layer.

    Be descriptive, focusing on nouns and visually descriptive phrases.

    Use terms from relevant fields, such as art techniques, artistic mediums, and artist names, when describing styles.

    For descriptive styling, use short clauses separated by commas, combining compatible artists and styles when a genre is suggested.

    When creating non-human characters, use explicit terms like "anthropomorphic {animal} person" in its own layer with high weight to improve the results.

    Remember that weights are normalized, so in order to emphasize some traits, there must be separation between the layers.

    Stay within a token limit (e.g., 250 tokens) to ensure the entire list can be generated by ChatGPT.

Example:

Original prompt: Create a cute anthropomorphic fox character for a children's story, wearing a colorful outfit and holding a balloon.

    Anthropomorphic fox person ::8. Cute, friendly smile, bushy tail ::6. Colorful outfit, overalls, polka dot shirt ::4. Holding a balloon, floating, clouds ::3. Watercolor illustration, soft colors, gentle shading ::2. Castle in the background ::1.

Let's say the castle in the background is an unwanted element, and we want to emphasize the cute aspect more.

Adjusted prompt:

    Anthropomorphic fox person ::8. Cute, friendly smile, bushy tail ::9. Colorful outfit, overalls, polka dot shirt ::4. Holding a balloon, floating, clouds ::3. Watercolor illustration, soft colors, gentle shading ::2. No castle ::-1.

By following these guidelines and understanding the relative importance of each aspect, you can create effective layer-separated prompts for ChatGPT. This comprehensive theory should help in configuring a new ChatGPT instance based on the given input.