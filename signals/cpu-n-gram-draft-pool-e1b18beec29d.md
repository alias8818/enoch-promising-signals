# CPU N-Gram Draft Pool

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-draft-pool-e1b18beec29d`
Run ID: `cpu-n-gram-draft-pool-e1b18beec29d-20260529T201159365136+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/46409790d22f

## What looked useful

CPU n-gram pools are cheap and contain measurable local continuation signal, but the tested word-token greedy draft-pool form is too weak for long speculative drafts; future work should test short candidate use under a real model/tokenizer.

## Boundaries and scale limits

Small corpora, regex word/character tokenization, held-out continuation oracle only; no BPE tokenizer, target LLM, GPU validation pass, production traces, or end-to-end latency measurement.

## Claim scope

On two small public held-out text corpora, a CPU n-gram continuation pool produces microsecond-scale proposals and beats frequency baselines for next-token exact match, but greedy word-token draft rounds accept only about 0.15 to 0.26 tokens per validation round.

## Why it stopped

No-paper useful signal: this was a proxy/mechanism test, and word-token greedy draft acceptance was modest rather than publication-grade.

## Recommended next action

Run a bounded deepen follow-up integrating the n-gram pool with a small open-model tokenizer and target speculative decoding loop, then stop unless it shows real wall-clock speedup over no-draft and a simple draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-tokenized small-model n-gram speculative decoding benchmark
- Success threshold: At least 10% end-to-end tokens/s improvement over no-draft on a repetitive-domain corpus without regression on the general-domain control, with accepted tokens per validation round above 0.5 for the chosen draft length.
- Stop condition: Stop as negative if BPE-tokenized accepted tokens per validation round remains below 0.3 or measured tokens/s fails to improve by at least 5% over no-draft.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-draft-pool-e1b18beec29d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
