# NGramSpecDraft_CPU_Acceleration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ngramspecdraft-cpu-acceleration-f3d1046045de`
Run ID: `ngramspecdraft-cpu-acceleration-f3d1046045de-20260603T223813809493+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7dfe5b51a415

## What looked useful

Indexed n-gram lookup is cheap enough on CPU to justify real decoder integration for byte/subword drafting, but word-level n-gram drafting is unlikely to be useful as a standalone accelerator.

## Boundaries and scale limits

This is an offline replay proxy over one small text corpus. It does not measure real LLM verifier cost, KV-cache effects, tokenizer behavior for a production model, batched serving, prompt diversity, or output quality invariance.

## Claim scope

On Tiny Shakespeare replay, a single-process Python indexed n-gram drafter can generate CPU draft proposals at 140k-360k lookups/s with microsecond median latency; byte-level contexts n=4-6 produce 45.98%-47.62% proxy target-call reduction, while word-level contexts are too sparse at 0.09%-7.14% proxy reduction.

## Why it stopped

No-paper closure: this run provides bounded replay evidence only, not end-to-end model-serving acceleration or publication-grade validation.

## Recommended next action

Run a bounded GPT-2-small CPU greedy-decoding integration that compares indexed byte/subword n-gram speculative drafting against standard decoding on fixed prompts for tokens/s, verifier acceptance, and identical-output correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small CPU integration for indexed n-gram speculative drafting
- Success threshold: At least 10% end-to-end tokens/s improvement over baseline greedy decoding on CPU with deterministic output equivalence and at least 0.5 accepted draft tokens per target-model call.
- Stop condition: Stop if integration overhead erases speedup, if accepted draft tokens fall below 0.2 per target-model call across the prompt suite, or if deterministic output equivalence cannot be maintained.

## Evidence references

- Artifact root: `<local-path>/projects/ngramspecdraft-cpu-acceleration-f3d1046045de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
