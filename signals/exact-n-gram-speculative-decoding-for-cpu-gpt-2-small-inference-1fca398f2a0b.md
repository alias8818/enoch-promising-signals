# Exact n-gram speculative decoding for CPU GPT-2-small inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-n-gram-speculative-decoding-for-cpu-gpt-2-small-inference-1fca398f2a0b`
Run ID: `exact-n-gram-speculative-decoding-for-cpu-gpt-2-small-inference-1fca398f2a0b-20260604T123031657524+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6ed8e4d03c38

## What looked useful

Exact prompt/context n-gram drafting is mechanically valid for greedy decoding, but acceptance rate determines viability. Repetitive prompts reached 1.73x-2.43x speedup with 0.85-0.92 mean acceptance; natural prompts slowed to 0.87x-0.92x because verification consumed many extra model input tokens despite fewer model calls.

## Boundaries and scale limits

Eight total prompts, 64 generated tokens each, greedy decoding only, CPU PyTorch/Transformers implementation, small natural and repetitive prompt sets rather than a full held-out corpus or production serving stack.

## Claim scope

On this CPU worker with GPT-2-small greedy decoding for 64 generated tokens, exact n-gram speculative decoding preserved output identity and improved throughput only for deliberately repetitive prompts, not for the small natural-prompt set.

## Why it stopped

Direct small-scale CPU GPT-2-small evidence is mixed: exactness and repetitive-context acceleration are supported, but the general natural-text speedup hypothesis is not supported by this bounded benchmark.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add adaptive draft gating and evaluate on a real held-out text corpus before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive gated exact n-gram speculation on held-out CPU GPT-2-small decoding
- Success threshold: At least 1.10x geometric mean throughput versus greedy on the held-out corpus, no prompt subset below 0.98x, and 100% exact output identity for greedy decoding.
- Stop condition: Stop if adaptive gating cannot avoid slowdowns on low-acceptance natural prompts or if exact output identity fails.

## Evidence references

- Artifact root: `<local-path>/projects/exact-n-gram-speculative-decoding-for-cpu-gpt-2-small-inference-1fca398f2a0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
