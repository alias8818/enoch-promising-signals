# N-gram speculative draft for CPU local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-cpu-local-inference-bc68fee60905`
Run ID: `n-gram-speculative-draft-for-cpu-local-inference-bc68fee60905-20260527T120301946293+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/904c3dfc2ffb

## What looked useful

The mechanism is real but weak in this bounded setting: best first-token acceptance was 14.1% on Tiny Shakespeare and 21.3% on Alice, full-draft acceptance was 0.0% for the best configurations, and most verifier calls rejected the first drafted token.

## Boundaries and scale limits

This was a trace-level proxy, not an end-to-end CPU LLM benchmark. It used two small corpora, static train/test n-grams, no real LLM tokenizer, no verifier runtime, and no sampling-policy interaction.

## Claim scope

On two small held-out text traces with a regex word/punctuation tokenizer, deterministic static n-gram drafting is microsecond-cheap and yields modest idealized verifier-call reductions of 1.16x to 1.29x, but median accepted draft length is zero.

## Why it stopped

Trace evidence supports only modest ideal verifier-call reduction and does not establish end-to-end CPU inference speedup.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded step is an end-to-end llama.cpp or equivalent CPU runtime test with the model tokenizer and real tokens/s measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LLM n-gram speculative decoding benchmark
- Success threshold: At least 1.10x median wall-clock tokens/s improvement over no-draft baseline on a predefined repetitive/local-domain prompt set, with no regression larger than 5% on the open-ended control set.
- Stop condition: Stop if end-to-end tokens/s improvement is below 1.05x on the repetitive prompt set or if verifier integration overhead erases the idealized trace-level target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-local-inference-bc68fee60905`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
