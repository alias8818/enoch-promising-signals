# Layer-swept verifier-loop test for early-hidden linear draft probes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-swept-verifier-loop-test-for-early-hidden-linear-dra-022b981127`
Run ID: `layer-swept-verifier-loop-test-for-early-hidden-linear-dra-022b981127-20260525T011601114871+0000`

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

- Parent run decision: Trained Linear Probe from Early Hidden State as Draft: enoch://control-plane/projects/trained-linear-probe-from-early-hidden-state-as-draft-033b200362c2/runs/trained-linear-probe-from-early-hidden-state-as-draft-033b200362c2-20260525T000358268154+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/da180e9f4a95

## What looked useful

Early hidden states were linearly decodable enough for 71.3-75.85% verifier acceptance across three seeds and beat the best unigram/previous-token baseline by at least 21.2 percentage points, but they failed the predeclared 2x-baseline success threshold.

## Boundaries and scale limits

Toy causal teacher only; no pretrained transformer, no real text corpus, no KV-cache or end-to-end speculative decoding latency, and no measured speedup after probe overhead.

## Claim scope

In a self-contained toy frozen causal teacher with 64-token vocabulary, 96-dimensional hidden states, 8 nonlinear residual layers, 6000 probe-training examples, and 2000 held-out examples per seed, layer-swept linear probes from early layers matched the teacher final top-1 token with mean verifier acceptance 0.734 across three seeds.

## Why it stopped

No-paper useful signal: the controlled direct toy test supports a mechanism but fails the predeclared 2x-baseline success threshold and is not real-model publication evidence.

## Recommended next action

Run a bounded direct follow-up on a real small pretrained causal LM with real prompts, measuring early-layer probe acceptance and probe overhead against a strong cheap-token baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LM layer-swept verifier-loop test for early hidden linear draft probes
- Success threshold: Best early-layer probe reaches at least 0.55 verifier acceptance, beats the best cheap baseline by at least 0.15 absolute acceptance, and has estimated net speedup above 1.10x after probe overhead on the tested small LM.
- Stop condition: Stop if early-layer acceptance is below 0.45, improves over the best cheap baseline by less than 0.05 absolute, or probe overhead makes estimated speedup <= 1.0x.

## Evidence references

- Artifact root: `<local-path>/projects/layer-swept-verifier-loop-test-for-early-hidden-linear-dra-022b981127`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
