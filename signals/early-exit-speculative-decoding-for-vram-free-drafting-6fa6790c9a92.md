# Early-Exit Speculative Decoding for VRAM-Free Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-speculative-decoding-for-vram-free-drafting-6fa6790c9a92`
Run ID: `early-exit-speculative-decoding-for-vram-free-drafting-6fa6790c9a92-20260526T021901452146+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

Intermediate distributions improved with depth but remained too weak at useful exits: gpt2 layer 8/12 reached 0.299 generated-context expected sample acceptance and layer 11/12 reached 0.518, while optimistic k=2 throughput estimates stayed below baseline for all tested exits.

## Boundaries and scale limits

Tested sshleifer/tiny-gpt2 smoke, distilgpt2, and gpt2 on 12 prompts with short generated continuations. Did not implement optimized KV-cache speculative serving, did not test 7B+ models, and did not train auxiliary early-exit heads.

## Claim scope

Raw untrained early-exit logits, produced by applying the target model final norm and LM head to intermediate GPT-2-family hidden states, did not provide enough speculative acceptance to justify VRAM-free drafting in bounded local tests.

## Why it stopped

Proxy/local early falsification: raw intermediate logits were directly tested for acceptance quality and were insufficient for speedup under favorable accounting; full production validation would require an optimized speculative decoder and larger models.

## Recommended next action

Run a bounded follow-up that trains a lightweight calibrated early-exit head and requires >=0.75 expected acceptance by <= half depth plus actual KV-cache throughput accounting before considering larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Early-Exit Heads for VRAM-Light Speculative Drafting
- Success threshold: At <= half model depth, held-out generated-context expected sample acceptance >=0.75 and measured end-to-end throughput >=1.2x baseline with no separate draft model weights.
- Stop condition: Stop if acceptance remains below 0.60 at <= half depth or measured throughput is <=1.0x after KV-cache accounting.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-speculative-decoding-for-vram-free-drafting-6fa6790c9a92`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
