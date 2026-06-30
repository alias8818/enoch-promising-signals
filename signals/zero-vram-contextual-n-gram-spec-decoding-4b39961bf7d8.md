# Zero-VRAM Contextual N-Gram Spec Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zero-vram-contextual-n-gram-spec-decoding-4b39961bf7d8`
Run ID: `zero-vram-contextual-n-gram-spec-decoding-4b39961bf7d8-20260524T215104504880+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f1cc68664d7

## What looked useful

Zero-draft-VRAM contextual n-gram speculation has a measurable bounded signal, but high first-token rejection rates are the central risk: the best call simulation reduces target calls by 19.85%, while 79.16% of proposal calls reject at the first token. GPT-2 greedy verification over 256 proposals showed recent contextual drafts at 0.2412 token accept rate versus 0.2100 for same-suffix random controls.

## Boundaries and scale limits

No integrated wall-clock decoder was benchmarked. The main target-call result is a ground-truth/oracle simulation, not an end-to-end serving measurement. The direct model verifier used GPT-2 and only 256 proposals on one repeat-heavy literary corpus, so results may not transfer to larger target models, chat/code workloads, or low-overhead production decoding.

## Claim scope

On GPT-2-tokenized Tiny Shakespeare with online no-future-leak contextual suffix matching, CPU/RAM n-gram drafts can produce accepted speculative tokens and an oracle ground-truth simulation reaches 1.2476 generated tokens per target call for draft_len 8/max_n 3. A 256-proposal GPT-2 greedy verifier probe also accepts more recent contextual proposals than same-suffix random controls.

## Why it stopped

Proxy and small direct verifier evidence supports the mechanism but does not establish end-to-end speedup; this is not a full validation or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is an integrated decoder benchmark that measures wall-clock tokens/sec including CPU lookup and verifier overhead on GPT-2 or Pythia-70M before attempting larger models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated Wall-Clock Benchmark for Zero-VRAM Contextual N-Gram Speculation
- Success threshold: At least 5% wall-clock tokens/sec improvement over greedy decoding with no increase in output mismatch rate, plus proposal overhead below the saved verifier time on the repeat-heavy corpus.
- Stop condition: Stop as negative if integrated wall-clock speedup is below 2% or if CPU lookup/verification overhead consumes the simulated target-call savings on the small-model benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/zero-vram-contextual-n-gram-spec-decoding-4b39961bf7d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
