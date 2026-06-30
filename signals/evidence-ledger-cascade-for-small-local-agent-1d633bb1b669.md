# Evidence-ledger cascade for small local agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-cascade-for-small-local-agent-1d633bb1b669`
Run ID: `evidence-ledger-cascade-for-small-local-agent-1d633bb1b669-20260607T095425219404+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3381bf24a3dd

## What looked useful

Across 48,000 synthetic examples, the ledger cascade reduced false-answer rate in every condition. With one support document it often traded away coverage under high contradiction rates; with two support documents it kept about 0.985-0.999 coverage and improved accuracy by 0.107-0.150 absolute while keeping false-answer rate near zero.

## Boundaries and scale limits

Proxy-only synthetic benchmark; no actual local LLM, no real-world corpus, no human grading, no paraphrase-heavy evidence, and no multi-turn tool-use evaluation. Results should not be treated as publication-grade or full validation.

## Claim scope

In a synthetic local retrieval/extraction benchmark, an evidence-ledger cascade with contradiction-aware abstention reduced false answers versus a top-hit baseline; with two support snippets it also preserved high coverage and improved raw accuracy.

## Why it stopped

Closed as no-paper useful signal because the current result is synthetic/proxy evidence, not direct full validation with a real small local agent.

## Recommended next action

Run a bounded direct-evidence follow-up using an actual small local LLM on a held-out natural-language evidence corpus, comparing top-hit RAG, answer-then-verify, and evidence-ledger cascade under identical retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small local LLM evidence-ledger cascade on natural evidence tasks
- Success threshold: Ledger cascade reduces false-answer rate by at least 30 percent relative to the best baseline while preserving at least 0.85 coverage and not reducing raw accuracy by more than 0.03 absolute.
- Stop condition: Stop if the local LLM ledger fails to reduce false-answer rate by at least 10 percent on a 100-example smoke set, or if extraction/citation failures prevent reliable scoring.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-cascade-for-small-local-agent-1d633bb1b669`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
