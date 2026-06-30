# Rolling N-gram Cache Lookahead

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `rolling-n-gram-cache-lookahead-29c12306aaed`
Run ID: `rolling-n-gram-cache-lookahead-29c12306aaed-20260529T081713137906+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c0c56bfae25

## What looked useful

The rolling n-gram cache mechanism passes a bounded sanity check: it is inert on random tokens, strong on repeated or templated streams, and gives a smaller but persistent positive signal on natural text. Cache window size matters; 512-8192 token windows retain part of the natural-text effect.

## Boundaries and scale limits

This run measured token-stream exact-match acceptance and a verifier-call proxy only. It did not run an LLM verifier, measure GPU wall-clock speedup, evaluate sampling behavior, compare against learned drafters, or quantify production cache overhead. Corpora were small and unbounded-cache results overstate what a fixed-memory serving implementation may achieve.

## Claim scope

On GPT-2-tokenized synthetic and public text streams up to 160k tokens, an exact rolling n-gram cache can draft repeated continuations with useful acceptance when the stream has repeated local contexts. In this proxy, lookahead-4 unbounded-cache verifier-call reduction was 0.6824 on repeated copy blocks, 0.5420 on templated logs, 0.1803 on Tiny Shakespeare, 0.2032 on Alice, and 0.0000 on iid random tokens.

## Why it stopped

Closed as a no-paper useful signal because the evidence supports the cache mechanism in a proxy token-stream setting but is not direct LLM serving evidence.

## Recommended next action

Run a bounded deepen follow-up that implements rolling n-gram cache lookahead as a drafter around GPT-2-small-class decoding and measures actual tokens/sec, accepted draft length, quality parity, and memory overhead versus no-draft and prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2 Decoder Test for Rolling N-gram Cache Lookahead
- Success threshold: At least 10% wall-clock tokens/sec improvement over no-draft on a public repeat-containing corpus with exact greedy parity, plus no regression on a natural-text control and documented memory overhead under a fixed cache window.
- Stop condition: Stop if accepted draft length is below 0.1 tokens/step or wall-clock speedup is under 3% in the repeat-heavy corpus after cache maintenance overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-n-gram-cache-lookahead-29c12306aaed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
