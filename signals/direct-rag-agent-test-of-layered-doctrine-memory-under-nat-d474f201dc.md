# Direct RAG-Agent Test of Layered Doctrine Memory Under Natural-Language Updates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-rag-agent-test-of-layered-doctrine-memory-under-nat-d474f201dc`
Run ID: `direct-rag-agent-test-of-layered-doctrine-memory-under-nat-d474f201dc-20260620T035004022821+0000`

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

- Parent run decision: Layered Memory with Operator-Doctrine Updates: enoch://control-plane/projects/layered-memory-with-operator-doctrine-updates-eea64e36d136/runs/layered-memory-with-operator-doctrine-updates-eea64e36d136-20260620T031303171102+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2b41b650352d

## What looked useful

Layered doctrine memory directly fixes stale-rule retrieval in the controlled setting, but robust natural-language update extraction is the bottleneck. The result supports a bounded mechanism, not publication readiness.

## Boundaries and scale limits

Synthetic corpus only; deterministic parser; no real LLM agent, real doctrine corpus, human labels, noisy contradiction handling, or long-running memory persistence test. Held-out natural-language update phrasings reduced layered accuracy to 50%.

## Claim scope

In a controlled synthetic doctrine stream with parser-covered natural-language update templates, layered/versioned doctrine memory answered current-doctrine questions at 100% accuracy across 5 seeds and materially outperformed append-only flat TF-IDF RAG baselines.

## Why it stopped

Tier 1 controlled direct test completed with useful mechanism support, but stress testing showed parser brittleness, so this is no-paper evidence rather than a full validation.

## Recommended next action

Run a bounded deepen test replacing the deterministic update parser with a held-out robust extractor or LLM-structured extraction layer, then require high current-doctrine accuracy on unseen update phrasings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Doctrine Memory With Robust Held-Out Natural-Language Update Extraction
- Success threshold: On at least 200 current-doctrine queries, layered memory with robust extraction reaches >=90% accuracy on held-out update phrasings and beats the best flat RAG baseline by >=20 percentage points.
- Stop condition: Stop as negative if extraction-caused misses keep current-doctrine accuracy below 80% or if the gain over the best flat baseline is under 10 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/direct-rag-agent-test-of-layered-doctrine-memory-under-nat-d474f201dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
