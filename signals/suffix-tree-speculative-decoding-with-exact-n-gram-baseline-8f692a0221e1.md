# Suffix-tree speculative decoding with exact n-gram baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-with-exact-n-gram-baseline-8f692a0221e1`
Run ID: `suffix-tree-speculative-decoding-with-exact-n-gram-baseline-8f692a0221e1-20260628T165611982589+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/27a841f3269d

## What looked useful

Compare suffix-tree-style speculative decoders against abstaining exact n-gram baselines. Longest-match retrieval helped on repeated structure (+4.48% accepted tokens over ngram_4) and Markov-like data (+56.91% relative but only 0.2385 accepted tokens/query), but it was 24-37x slower than fixed n-gram lookup and nearly useless on random data unless it abstains on weak short-context matches.

## Boundaries and scale limits

25k train tokens plus 10k eval tokens per synthetic regime, 2k exact-verification queries per regime, draft length 16, no neural LM verifier, no real tokenizer corpus, no GPU serving path, and a bounded suffix-context dictionary rather than a production compressed suffix tree.

## Claim scope

Bounded synthetic cache-proposal proxy: longest exact suffix matching can increase accepted draft tokens over a fixed exact n-gram baseline on repetitive and Markov-like token streams, but the gain is small or low in absolute terms and comes with substantially higher lookup overhead in this implementation.

## Why it stopped

Proxy/local evidence is mixed: the mechanism improves accepted-token counts in structured synthetic regimes, but not enough and not directly enough to support a paper or full serving claim.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded real-corpus small-LM verifier experiment with abstention thresholds before considering any larger GB10 serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-LM verifier test for suffix longest-match speculative decoding with abstention
- Success threshold: At least 15% more accepted tokens per verifier pass than the best exact n-gram baseline on real text, with no worse than 5% end-to-end latency regression in the local verifier loop.
- Stop condition: Stop if suffix longest-match fails to beat the best exact n-gram baseline by 10% accepted tokens per verifier pass or if abstention cannot remove low-value proposals without erasing the acceptance gain.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-with-exact-n-gram-baseline-8f692a0221e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
