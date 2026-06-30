# Self-Speculative Decoding via Early Layer Exit on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-layer-exit-on-cpu-6eb6aaca1043`
Run ID: `self-speculative-decoding-via-early-layer-exit-on-cpu-6eb6aaca1043-20260523T083006730982+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c52acf841528

## What looked useful

Early layers 1/3/4 had 0.0%, 1.56%, and 4.69% top-1 agreement; layer 5 reached 39.06% but modeled only 0.59x best-case speedup at block size 1 and worse for larger blocks. The raw early-exit mechanism is therefore not viable as tested.

## Boundaries and scale limits

Tested 4 prompts, 64 generated tokens total, distilgpt2 only, greedy decoding only, block sizes 1/2/4, and a modeled rather than implemented partial-layer draft path. This is not a full production decoder benchmark or large-model validation.

## Claim scope

On a CPU worker, raw intermediate hidden states from pretrained distilgpt2 with the shared LM head do not provide enough greedy top-1 agreement for early-layer self-speculative decoding to beat normal greedy decoding under a measured verification plus proportional draft-cost model.

## Why it stopped

Proxy/early falsification rather than full validation: direct agreement and verification timing on distilgpt2 show insufficient accepted drafts, while partial draft runtime was modeled rather than implemented.

## Recommended next action

Stop this raw shared-head early-exit approach; only pursue a bounded follow-up that trains or calibrates early-exit heads and tests the same CPU draft/verify metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Early-Exit Heads for CPU Self-Speculative Decoding
- Success threshold: At least one mid-layer/block-size setting must show >=1.15x measured end-to-end CPU speedup over greedy decoding with exact greedy-output preservation across at least 512 held-out generated tokens.
- Stop condition: Stop if calibrated mid-layer agreement remains below 70% for block size 1 or if measured partial-draft plus verification latency is not at least 10% faster than greedy after 512 held-out generated tokens.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-layer-exit-on-cpu-6eb6aaca1043`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
