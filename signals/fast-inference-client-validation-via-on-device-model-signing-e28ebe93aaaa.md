# Fast Inference Client Validation via On-Device Model Signing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fast-inference-client-validation-via-on-device-model-signing-e28ebe93aaaa`
Run ID: `fast-inference-client-validation-via-on-device-model-signing-e28ebe93aaaa-20260607T040908995361+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6a20286ef314

## What looked useful

Signature verification itself is not the bottleneck: Ed25519 and ECDSA P-256 verified signed digests in about 0.04 ms median and RSA-PSS-2048 in about 0.021 ms median. Full-content validation is bytes-bound: SHA-256 over 256 MiB took 107.9 ms median and Merkle validation over 1 MiB chunks took 115.5 ms median. This supports signed-manifest checks for fast client gating and falsifies per-request full-model rehashing for low-latency inference paths.

## Boundaries and scale limits

Synthetic byte artifacts only; largest direct artifact was 256 MiB; no real model format, mobile device, secure enclave/TEE, revocation path, model registry, storage cold-cache behavior, or production inference client was tested. 512 MiB to 8 GiB costs are extrapolated from 256 MiB throughput.

## Claim scope

On this GB10/aarch64 host, client-side verification of a signed model manifest or precomputed content digest is tens of microseconds, while full artifact hashing for synthetic 16-256 MiB model-sized blobs is linear at about 2.37 GiB/s and therefore appropriate for load/update validation rather than every inference request.

## Why it stopped

Bounded local synthetic benchmark produced a useful mechanism signal but not direct publication-grade validation of an inference client or target device deployment.

## Recommended next action

Run a bounded deepen test on real model files using cold/warm mmap or streaming I/O and an actual client startup path; stop treating this run as paper-ready because it is synthetic and mechanism-level only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real model file startup validation with mmap and signed manifests
- Success threshold: For warm-cache startup, signed-manifest verification plus any required cached-digest check adds less than 5 percent to median client startup/first-inference latency for each tested model, and tampered bytes/metadata are always rejected.
- Stop condition: Stop if cold or warm validation overhead exceeds 20 percent of startup/first-inference latency for medium and large models, or if the client cannot persist and bind content digests safely across updates.

## Evidence references

- Artifact root: `<local-path>/projects/fast-inference-client-validation-via-on-device-model-signing-e28ebe93aaaa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
