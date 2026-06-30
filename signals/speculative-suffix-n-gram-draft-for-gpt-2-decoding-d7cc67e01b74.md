# Speculative Suffix: N-Gram Draft for GPT-2 Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74`
Run ID: `speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74-20260609T031634307240+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

Main run was exact on all prompts, accepted 76.85% of drafted tokens, reduced target forwards by 35.87%, and reached 1.45x mean throughput versus warmed cached greedy. Gamma and suffix-min sweeps showed coherent tradeoffs, with unigram suffix matches causing more rejections.

## Boundaries and scale limits

Small hand-curated prompt set, GPT-2 small only, greedy decoding only, single GB10 process, no batching, no held-out corpus, no larger-model or production serving validation.

## Claim scope

On a 16-prompt local GPT-2-small greedy decoding benchmark, exact suffix n-gram speculative drafting can preserve greedy outputs while reducing target-model forward calls and improving mean single-process CUDA throughput, especially on repetitive/local-copy contexts.

## Why it stopped

Evidence supports a bounded mechanism but is not publication-grade: it uses a small curated prompt set and does not validate larger models, held-out corpora, batching, sampling, or production serving behavior.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded step is a held-out corpus benchmark with a production cache-state implementation and batching controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out GPT-2 suffix n-gram speculative decoding benchmark
- Success threshold: Exact output match on all evaluated greedy decodes, at least 20% mean target-forward reduction, at least 15% p50 throughput improvement, and no more than 5% p10 throughput regression on held-out prompts.
- Stop condition: Stop if held-out acceptance falls below 40%, target-forward reduction falls below 10%, or p50 throughput fails to beat cached greedy after cache-rebuild overhead is removed.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-suffix-n-gram-draft-for-gpt-2-decoding-d7cc67e01b74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
