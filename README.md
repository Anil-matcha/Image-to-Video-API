# Image to Video API

Turn an image into a generated video. Compare first-frame, optional last-frame, duration, resolution, and quality controls across supported Muapi models.

[Muapi Image to Video API landing page](https://muapi.ai/image-to-video-api) · [API reference](https://muapi.ai/docs/api-reference) · [Create an API key](https://muapi.ai/access-keys)

## Related Projects

- [AI-Video-API](https://github.com/Anil-matcha/AI-Video-API)
- [AI-Character-Consistency-API](https://github.com/Anil-matcha/AI-Character-Consistency-API)

## What this API covers

Use the endpoint that matches the task and input media. The routes below are enabled Muapi model IDs checked against the current model catalog; availability, request fields, and pricing can change, so verify the linked landing page and endpoint schema before production use.

| Endpoint | Purpose | Category |
|---|---|---|
| `wan2.2-image-to-video` | Image to Video | `Image to Video` |
| `seedance-2.5-image-to-video` | Image to Video | `Image to Video` |
| `kling-v3.0-pro-image-to-video` | Image to Video [Pro] | `Image to Video` |

## Quick start

Muapi uses an asynchronous REST contract. Submit a JSON request with your API key, save the returned `request_id`, then poll the result endpoint. Replace sample URLs with files you control and fields with values supported by the selected endpoint.

```bash
curl -X POST https://api.muapi.ai/api/v1/wan2.2-image-to-video \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MUAPI_API_KEY" \
  -d '{
    "prompt": "A close-up video of a young woman smiling gently in the rain, with raindrops glistening on her face and eyelashes. The camera focuses on the delicate details of her expression and the shimmering water droplets, while soft light softly reflects off her skin, emphasizing the rainy atmosphere.",
    "image_url": "https://example.com/replace-with-your-file"
  }'
```

### Request fields in this example

| Field | Requirement | Notes |
|---|---|---|
| `prompt` | Required | The prompt to generate the video |
| `image_url` | Required | URL of the input image. |

### Poll for the result

```bash
curl "https://api.muapi.ai/api/v1/predictions/$REQUEST_ID/result" \
  -H "x-api-key: $MUAPI_API_KEY"
```

Poll until the task status is `completed` or `failed`. Read the response’s output URLs on completion; download outputs you need to retain, since provider-hosted URLs may expire.

## Choosing an endpoint

Compare supported inputs and output behavior first, then resolution, duration, quality controls, latency, and price for your use case. Similar names do not guarantee interchangeable request schemas. This repository lists representative routes; the [landing page](https://muapi.ai/image-to-video-api) contains the current task-specific explanation, examples, and pricing context.

## Errors and production notes

- Keep the API key in an environment variable; do not commit credentials.
- Validate inputs against the selected endpoint’s current schema.
- Handle non-success HTTP responses and failed task states explicitly.
- Retry only when appropriate for the error; avoid submitting duplicate billable jobs after a timeout without checking the original `request_id`.
- Confirm current pricing and availability on the Muapi page before estimating production cost.

## Links

- [Muapi Image to Video API](https://muapi.ai/image-to-video-api)
- [API reference](https://muapi.ai/docs/api-reference)
- [Playground](https://muapi.ai/playground)
- [API key setup](https://muapi.ai/access-keys)
